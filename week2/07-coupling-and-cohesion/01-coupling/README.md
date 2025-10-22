# 01. 결합도(Coupling): 느슨하게 연결하고 유연하게 만들기

소프트웨어 설계에서 **결합도(Coupling)**는 **'한 모듈(클래스, 함수 등)이 다른 모듈에 얼마나 의존하고 연결되어 있는가'**를 나타내는 척도입니다. 두 모듈이 서로에 대해 너무 많은 것을 알고 있다면, '결합도가 높다(Tightly Coupled)'고 말합니다.

좋은 소프트웨어 설계는 **'낮은 결합도(Loose Coupling)'**를 지향합니다. 이는 각 모듈이 독립적으로 존재하여, 하나의 모듈을 수정해도 다른 모듈에 미치는 영향을 최소화하는 것을 목표로 합니다.

### 왜 낮은 결합도가 중요한가?

-   **유지보수성**: 결합도가 낮으면, 특정 기능의 코드를 수정할 때 다른 코드를 신경 쓸 필요가 줄어듭니다. 버그 수정이 쉬워지고, 의도치 않은 부작용(side effect)이 발생할 위험이 크게 감소합니다.
-   **재사용성**: 각 모듈이 독립적이므로, 필요한 모듈을 가져다가 다른 프로젝트나 시스템의 다른 부분에서 쉽게 재사용할 수 있습니다.
-   **테스트 용이성**: 결합도가 높은 코드는 테스트하기 매우 어렵습니다. `A`를 테스트하기 위해 `B`, `C`, `D`를 모두 준비해야 하기 때문입니다. 반면, 결합도가 낮은 코드는 테스트하려는 모듈만 독립적으로 떼어내어 테스트(단위 테스트)하기 훨씬 쉽습니다.

### 코드 예시: 높은 결합도 vs 낮은 결합도

쇼핑몰의 주문 처리 시스템을 예로 들어보겠습니다.

#### 높은 결합도 (Tightly Coupled) - 나쁜 예

```python
class OrderProcessor:
    def process(self, order_id, customer_name, items, credit_card_number, cvv):
        # 1. 주문 정보를 직접 처리
        print(f"주문({order_id}) 처리 중...")
        
        # 2. 결제 시스템의 세부 구현을 직접 알고 사용함
        print(f"{credit_card_number} 카드로 결제를 시도합니다.")
        payment_success = self._process_credit_card(credit_card_number, cvv)
        
        if payment_success:
            # 3. 배송 시스템의 세부 구현을 직접 알고 사용함
            print(f"{customer_name}님에게 배송을 시작합니다.")
            self._start_shipping(customer_name, items)
            return "주문 성공"
        else:
            return "결제 실패"

    def _process_credit_card(self, card_number, cvv):
        # 신용카드 결제를 처리하는 복잡한 로직...
        print("PG사(결제대행사)와 통신 중...")
        return True

    def _start_shipping(self, customer_name, items):
        # 배송을 처리하는 복잡한 로직...
        print("물류 창고에 배송 요청 전송 중...")
        return "tracking_id_123"

# 사용 예
processor = OrderProcessor()
processor.process(101, "Alice", ["Apple", "Banana"], "1234-5678-...", "123")
```

-   **문제점**: `OrderProcessor` 클래스가 '결제'와 '배송'의 모든 세부적인 과정을 직접 알고 책임지고 있습니다. 만약 결제 방식(예: 신용카드 -> 간편결제)이 바뀌거나 배송 업체가 바뀌면, `OrderProcessor` 클래스의 코드를 직접 수정해야만 합니다. 이는 OCP(개방-폐쇄 원칙)를 위반합니다.

#### 낮은 결합도 (Loosely Coupled) - 좋은 예

이제 각 책임을 별도의 클래스로 분리하고, '추상화'에 의존하도록 리팩토링해봅시다.

```python
# --- 각 모듈을 독립적으로 분리 ---

class PaymentGateway:
    def process_payment(self, amount, credit_card_number, cvv):
        print(f"{credit_card_number} 카드로 {amount}원 결제를 시도합니다.")
        print("PG사(결제대행사)와 통신 중...")
        return True

class ShippingService:
    def arrange_shipping(self, customer_name, items):
        print(f"{customer_name}님에게 {items} 배송을 시작합니다.")
        print("물류 창고에 배송 요청 전송 중...")
        return "tracking_id_456"

# --- 메인 로직은 추상화에 의존 ---

class OrderProcessor:
    # 생성될 때 외부에서 '의존성'을 주입받음 (Dependency Injection)
    def __init__(self, payment_gateway, shipping_service):
        self.payment_gateway = payment_gateway
        self.shipping_service = shipping_service

    def process(self, order, amount):
        print(f"주문({order['id']}) 처리 중...")
        
        payment_success = self.payment_gateway.process_payment(
            amount, 
            order['credit_card'], 
            order['cvv']
        )
        
        if payment_success:
            self.shipping_service.arrange_shipping(
                order['customer_name'], 
                order['items']
            )
            return "주문 성공"
        else:
            return "결제 실패"

# 사용 예
# 각 모듈의 인스턴스를 생성하고, OrderProcessor에 '주입'해줌
payment_gateway = PaymentGateway()
shipping_service = ShippingService()
processor = OrderProcessor(payment_gateway, shipping_service)

my_order = {
    'id': 102,
    'customer_name': 'Bob',
    'items': ['Orange', 'Milk'],
    'credit_card': '8765-4321-...',
    'cvv': '321',
}
processor.process(my_order, 5.00)
```
-   **개선점**: 이제 `OrderProcessor`는 `PaymentGateway`나 `ShippingService`의 **내부 구현을 전혀 알지 못합니다.** 단지 `process_payment`와 `arrange_shipping`이라는 **'인터페이스(메서드)'**가 존재한다는 사실에만 의존합니다.
-   **유연성**: 만약 `KakaoPayGateway`라는 새로운 결제 방식이 생겨도, `OrderProcessor`의 코드는 단 한 줄도 바꿀 필요가 없습니다. 그저 `OrderProcessor`를 생성할 때 `PaymentGateway()` 대신 `KakaoPayGateway()` 객체를 넣어주기만 하면 됩니다.

이처럼 **낮은 결합도**는 각 모듈이 맡은 책임에만 집중하게 하고, 변경이 발생했을 때 그 파급 효과를 최소화하여 시스템 전체를 유연하고 확장 가능하게 만드는 핵심적인 설계 원칙입니다.

---
**다음 세션**: [02. 응집도(Cohesion): 각자 자기 일만 잘하기](../02-cohesion/README.md)
