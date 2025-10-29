# 02. SOLID 원칙: 변경에 강한 파이썬 코드 만들기

SOLID는 객체지향 설계의 다섯 가지 원칙입니다. 파이썬에서도 동일하게 적용되며, **변경에 강하고 테스트하기 쉬운 코드**를 만드는 데 큰 도움이 됩니다.

## S: 단일 책임 원칙 (Single Responsibility Principle)
한 클래스/모듈은 단 하나의 책임(변경 이유)만 가져야 합니다.

```python
# 나쁜 예: 저장 + 검증 + 이메일 발송 책임이 한 클래스에
class UserService:
    def register(self, user):
        if "@" not in user.email:
            raise ValueError("invalid email")
        db.save(user)
        email.send_welcome(user.email)

# 좋은 예: 책임 분리
class UserValidator:
    def validate(self, user):
        if "@" not in user.email:
            raise ValueError("invalid email")

class UserRepository:
    def save(self, user):
        db.save(user)

class EmailService:
    def send_welcome(self, user):
        email.send_welcome(user.email)
```

## O: 개방-폐쇄 원칙 (Open-Closed Principle)
확장에는 열리고, 수정에는 닫혀 있어야 합니다.

```python
# 나쁜 예: 결제 방식 추가 시 if/elif 계속 증가
class Payment:
    def pay(self, method):
        if method == "card":
            ...
        elif method == "bank":
            ...

# 좋은 예: 다형성으로 확장
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CardPayment(PaymentMethod):
    def pay(self, amount):
        ...

class BankPayment(PaymentMethod):
    def pay(self, amount):
        ...

def checkout(method: PaymentMethod, amount: int):
    method.pay(amount)
```

## L: 리스코프 치환 원칙 (Liskov Substitution Principle)
상위 타입을 사용하는 곳에 하위 타입을 대체해도 동작이 깨지지 않아야 합니다.

```python
class Bird:
    def fly(self):
        ...

class Sparrow(Bird):
    def fly(self):
        ...

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError  # LSP 위반: Bird로서 fly를 기대했는데 깨짐
```

해결: 상위 타입을 재정의하여 "날 수 있는 새"와 "달리는 새"로 모델링을 분리합니다.

```python
class FlyingBird:
    def fly(self):
        ...

class RunningBird:
    def run(self):
        ...

class Sparrow(FlyingBird):
    def fly(self):
        ...

class Ostrich(RunningBird):
    def run(self):
        ...
```

## I: 인터페이스 분리 원칙 (Interface Segregation Principle)
클라이언트는 사용하지 않는 메서드에 의존하지 않아야 합니다.

```python
class Printer:
    def print(self):
        ...
    def scan(self):
        ...
    def fax(self):
        ...

# 단일 기능 인터페이스로 분리
class Printable:
    def print(self):
        ...

class Scannable:
    def scan(self):
        ...
```

## D: 의존성 역전 원칙 (Dependency Inversion Principle)
상위 모듈은 하위 모듈의 구현에 의존하지 말고 **추상화**에 의존해야 합니다.

```python
# 나쁜 예: 서비스가 구체 구현에 직접 의존
class ReportService:
    def __init__(self):
        self.storage = FileStorage()

# 좋은 예: 추상화에 의존 + 의존성 주입
class Storage:
    def save(self, data):
        raise NotImplementedError

class FileStorage(Storage):
    def save(self, data):
        ...

class ReportService:
    def __init__(self, storage: Storage):
        self.storage = storage
```

SOLID는 절대 규칙이 아니라 **유연하고 테스트 가능한 구조**를 위한 방향성입니다. 작은 리팩토링부터 적용해보세요.
