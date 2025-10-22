# 02. 대규모 테스트: 파라미터화를 통한 데이터 주도 테스트

하나의 기능을 테스트할 때, 우리는 보통 여러 가지 경우의 수를 확인해야 합니다.
-   이메일 유효성 검사: 정상적인 이메일, 아이디가 없는 이메일, `@`가 없는 이메일, ...
-   덧셈 함수: 양수끼리, 음수끼리, 양수와 음수, 0을 더하는 경우, ...

이런 경우, 각각의 케이스마다 테스트 함수를 하나씩 만드는 것은 엄청난 코드 중복을 유발하고 유지보수를 어렵게 만듭니다. `pytest`의 `@pytest.mark.parametrize`는 바로 이 문제를 해결하기 위한 강력한 기능으로, **테스트 로직은 하나로 유지**하되, **다양한 데이터를 주입하여 테스트를 여러 번 실행**하게 해줍니다.

### 파라미터화의 철학: 로직과 데이터의 분리

파라미터화의 핵심 철학은 **'무엇을 테스트할 것인가(로직)'**와 **'어떤 값으로 테스트할 것인가(데이터)'**를 명확하게 분리하는 것입니다.

-   **코드 중복 감소**: 비슷한 테스트 코드를 복사/붙여넣기 할 필요가 없어집니다.
-   **가독성 및 유지보수성 향상**: 테스트의 의도(로직)와 검증 범위(데이터)가 한눈에 들어옵니다. 새로운 테스트 케이스를 추가하거나 수정하는 것은 단지 데이터 목록에 한 줄을 추가/변경하는 작업이 됩니다.
-   **테스트의 완전성 증진**: 개발자는 무의식적으로 '성공하는 케이스' 위주로 테스트하려는 경향이 있습니다. 파라미터화는 다양한 실패 케이스, 엣지 케이스들을 데이터 목록으로 관리하게 함으로써, 더 꼼꼼하고 완전한 테스트를 작성하도록 유도합니다.

### 실습: 사용자 입력 유효성 검사하기

이번 실습에서는 이메일 형식과 비밀번호 강도를 검사하는 함수들을 다양한 입력값으로 테스트하며 파라미터화의 힘을 느껴보겠습니다.

**1. 실습 환경 및 파일 준비**
`week2/03-pytest-core-features/02-parametrization/` 폴더에서 이전과 같이 `my-param-test` 같은 실습 폴더를 만들고 `uv` 환경을 설정해주세요.

그 다음, `examples` 폴더의 `validation.py`와 `test_validation.py` 내용을 참고하여 `my-param-test` 폴더 안에 동일한 파일들을 생성합니다.

**`validation.py` (테스트 대상)**
```python
import re

def is_valid_email(email: str) -> bool:
    # ... (내용 생략) ...

def check_password_strength(password: str) -> str:
    # ... (내용 생략) ...
```

**`test_validation.py` (파라미터화된 테스트)**
```python
import pytest
from validation import is_valid_email, check_password_strength

@pytest.mark.parametrize("email, expected", [
    # --- 유효한 케이스들 ---
    ("test@example.com", True),
    ("user.name@domain.co.kr", True),
    # --- 유효하지 않은 케이스들 ---
    ("test@example", False),
    ("user name@example.com", False),
    (12345, False),
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected

@pytest.mark.parametrize("password, expected_strength", [
    ("1234567", "매우 약함"),          # 8자 미만
    ("longpassword", "약함"),          # 숫자 미포함
    ("strongpass123", "강함"),         # 8자 이상 + 숫자 포함
])
def test_check_password_strength(password, expected_strength):
    assert check_password_strength(password) == expected_strength
```

**2. 테스트 실행 및 분석**

터미널에서 `uv run pytest -v` 를 실행합니다.

**실행 결과:**
```
test_validation.py::test_is_valid_email[test@example.com-True] PASSED
test_validation.py::test_is_valid_email[user.name@domain.co.kr-True] PASSED
test_validation.py::test_is_valid_email[test@example-False] PASSED
... (총 5개의 is_valid_email 테스트 결과) ...
test_validation.py::test_check_password_strength[1234567-매우 약함] PASSED
test_validation.py::test_check_password_strength[longpassword-약함] PASSED
test_validation.py::test_check_password_strength[strongpass123-강함] PASSED
...
```

결과를 보면, `test_is_valid_email` 함수 하나가 5개의 다른 테스트 케이스로, `test_check_password_strength` 함수는 3개의 케이스로 실행된 것을 볼 수 있습니다. 각 테스트 케이스의 이름 뒤에는 `[... ]` 안에 사용된 파라미터 값이 표시되어, 어떤 데이터 조합으로 테스트가 실행되었고 성공/실패했는지 명확하게 알 수 있습니다.

만약 새로운 이메일 엣지 케이스를 발견했다면? `test_is_valid_email` 함수의 데이터 목록에 `("new.case@domain.com", True)` 한 줄만 추가하면 테스트 범위가 즉시 확장됩니다. 이것이 바로 데이터 주도 테스트의 힘입니다.

---
**다음 세션**: [03. 마커를 이용한 테스트 스위트 구성](../03-markers/README.md)
