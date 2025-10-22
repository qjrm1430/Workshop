# 02. 응집도(Cohesion): 각자 자기 일만 잘하기

**응집도(Cohesion)**는 **'하나의 모듈이 단 하나의 목적을 위해 얼마나 밀접하게 연관된 기능들로 구성되어 있는가'**를 나타내는 척도입니다. 어떤 클래스나 함수가 서로 관련 없는 여러 가지 기능들을 수행하고 있다면, '응집도가 낮다(Low Cohesion)'고 말합니다.

좋은 소프트웨어 설계는 **'높은 응집도(High Cohesion)'**를 지향합니다. 이는 각 모듈이 **'단 하나의 책임(Single Responsibility)'**만을 명확하게 가지는 것을 의미합니다.

### 왜 높은 응집도가 중요한가?

-   **가독성 및 이해 용이성**: 클래스나 함수의 이름만 보고도 그 역할이 명확하게 예측됩니다. 코드를 이해하고 분석하는 데 드는 정신적 비용이 크게 줄어듭니다.
-   **유지보수성**: 하나의 기능을 수정하기 위해 단 하나의 모듈만 보면 됩니다. 관련 없는 코드가 섞여 있지 않으므로 변경의 범위가 명확해지고, 실수를 할 가능성이 줄어듭니다.
-   **재사용성**: 특정 기능이 필요할 때, 해당 기능만을 담당하는 모듈을 가져다 쓰면 됩니다. 불필요한 다른 기능들이 섞여 들어오지 않습니다.

높은 응집도는 **단일 책임 원칙(Single Responsibility Principle, SRP)**과 거의 동일한 개념입니다. "하나의 클래스는 변경해야 할 이유가 단 하나여야 한다"는 SRP의 원칙이 바로 높은 응집도를 만드는 핵심 지침입니다.

### 코드 예시: 낮은 응집도 vs 높은 응집도

사용자 데이터를 관리하고 처리하는 시스템을 예로 들어보겠습니다.

#### 낮은 응집도 (Low Cohesion) - 나쁜 예

```python
class UserDataHandler:
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

    # 책임 1: 사용자 데이터 유효성 검사
    def is_valid_email(self):
        return "@" in self.user_email and "." in self.user_email.split('@')[1]

    # 책임 2: 데이터를 데이터베이스에 저장
    def save_to_database(self):
        # 데이터베이스 연결 및 저장 로직...
        print(f"데이터베이스에 {self.user_name} 정보를 저장합니다.")
        return True

    # 책임 3: 사용자에게 환영 이메일 발송
    def send_welcome_email(self):
        # 이메일 서버 연결 및 발송 로직...
        print(f"{self.user_email} 주소로 환영 이메일을 발송합니다.")
        return True
```
-   **문제점**: `UserDataHandler` 클래스는 너무 많은 일을 하고 있습니다. 이 클래스를 변경해야 할 이유는 최소 세 가지입니다. (1) 이메일 유효성 검사 규칙이 바뀔 때, (2) 데이터베이스 저장 방식이 바뀔 때, (3) 이메일 내용이나 발송 방식이 바뀔 때. 이렇게 관련 없는 책임들이 한 곳에 뭉쳐 있어 코드가 복잡해지고 재사용하기 어렵습니다.

#### 높은 응집도 (High Cohesion) - 좋은 예

이제 각 책임을 명확하게 분리하여 별도의 클래스로 만들어봅시다.

```python
# 책임 1: 사용자 데이터 자체를 표현 (데이터 객체)
class User:
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

# 책임 2: 사용자 데이터 유효성 검사
class UserValidator:
    def validate_email(self, user):
        print(f"{user.user_email}의 유효성을 검사합니다.")
        return "@" in user.user_email and "." in user.user_email.split('@')[1]

# 책임 3: 사용자 데이터를 저장소에 저장
class UserRepository:
    def save(self, user):
        print(f"데이터베이스에 {user.user_name} 정보를 저장합니다.")
        # 데이터베이스 연결 및 저장 로직...
        return True

# 책임 4: 사용자에게 이메일 발송
class EmailService:
    def send_welcome_email(self, user):
        print(f"{user.user_email} 주소로 환영 이메일을 발송합니다.")
        # 이메일 서버 연결 및 발송 로직...
        return True

# --- 각 모듈을 조합하여 사용 (오케스트레이션) ---
def register_new_user(user_id, user_name, user_email):
    user = User(user_id, user_name, user_email)
    
    validator = UserValidator()
    if not validator.validate_email(user):
        print("유효하지 않은 이메일입니다.")
        return

    repository = UserRepository()
    repository.save(user)
    
    email_service = EmailService()
    email_service.send_welcome_email(user)

# 사용 예
register_new_user(1, "Charlie", "charlie@example.com")
```

-   **개선점**: 이제 각 클래스는 이름만 봐도 무엇을 하는지 명확하게 알 수 있습니다.
    -   `User`: 사용자 데이터를 담는 역할만 합니다.
    -   `UserValidator`: 사용자 데이터의 유효성을 검사하는 책임만 집니다.
    -   `UserRepository`: 사용자 데이터를 저장하는 책임만 집니다.
    -   `EmailService`: 이메일을 보내는 책임만 집니다.
-   **유연성**: 만약 이메일 유효성 검사 로직을 더 정교하게 바꾸고 싶다면, `UserValidator` 클래스만 수정하면 됩니다. 다른 클래스들은 전혀 영향을 받지 않습니다.

### 결합도와 응집도의 관계: '주고받는' 사이

**결합도는 '모듈과 모듈 사이'의 관계**에 대한 것이고, **응집도는 '모듈 내부'의 이야기**입니다. 이 둘은 동전의 양면과 같아서, 보통 좋은 설계는 **'높은 응집도'**와 **'낮은 결합도'**를 함께 가집니다.

-   각 모듈이 **높은 응집도**를 가지고 자기 책임에만 집중하면,
-   자연스럽게 다른 모듈의 내부 구현에 신경 쓸 필요가 없어지므로 **낮은 결합도**를 가지게 됩니다.

이 두 가지 원칙을 항상 생각하며 코드를 작성하면, 더 깨끗하고 유연하며 테스트하기 쉬운, 한마디로 '잘 설계된' 소프트웨어를 만들 수 있습니다.

---
**워크숍을 마치며**
`week2` 워크숍을 통해 테스트의 기초부터 고급 기술, 그리고 좋은 설계 원칙까지 함께 살펴보았습니다. 이 지식들이 여러분의 개발 여정에 든든한 기반이 되기를 바랍니다.
