# 02. 첫 번째 테스트: 상세한 따라하기 가이드

이론은 충분히 배웠으니, 이제 직접 코드를 작성하고 실행하며 `pytest`의 강력함을 체감해볼 시간입니다. 이 세션에서는 여러분의 첫 번째 테스트를 성공적으로 작성하고 실행하는 모든 과정을 단계별로 아주 상세하게 안내합니다.

### 실습 목표

1.  `uv`를 사용하여 테스트 환경을 설정하고 `pytest`를 설치한다.
2.  테스트할 코드와 테스트 코드를 직접 작성하고 저장한다.
3.  `pytest`의 파일 탐색 규칙을 이해하고 적용한다.
4.  터미널에서 `pytest`를 실행하고 녹색 성공 메시지를 확인한다.

### 1단계: 실습 폴더 및 가상 환경 준비

먼저, 이번 세션의 실습을 진행할 별도의 폴더를 만들겠습니다. 터미널을 열고 `week2` 디렉토리로 이동한 후, 다음 명령어들을 순서대로 실행하세요.

```bash
# 1. 이번 실습을 위한 `my-first-test` 폴더를 만들고 그 안으로 이동합니다.
mkdir my-first-test
cd my-first-test

# 2. `uv`를 사용하여 가상 환경을 만들고 pytest를 설치합니다.
uv init
uv add --dev pytest
```

이제 `my-first-test` 폴더는 다음과 같은 구조를 가집니다.
```
my-first-test/
├── .venv/
└── pyproject.toml
```

### 2단계: 실습 파일 직접 작성하기

이제부터는 실제 개발자가 되어 테스트할 코드와 테스트 코드를 직접 작성해보겠습니다. `my-first-test` 폴더 안에 다음 두 개의 파일을 직접 만들어 코드를 입력해주세요.

**1. `math_functions.py` 파일 생성 (테스트 대상 코드):**
이 파일에는 우리가 테스트할 간단한 수학 함수들이 들어갑니다.

```python
# math_functions.py

def add(a, b):
    """두 숫자를 더한 값을 반환합니다."""
    return a + b

def subtract(a, b):
    """한 숫자에서 다른 숫자를 뺀 값을 반환합니다."""
    return a - b
```

**2. `test_math.py` 파일 생성 (테스트 코드):**
`add`와 `subtract` 함수가 올바르게 작동하는지 검증하는 테스트 코드입니다.

```python
# test_math.py

# 테스트 대상 함수들을 math_functions.py 파일로부터 가져옵니다.
from math_functions import add, subtract

# 'test_'로 시작하는 함수를 만들어 테스트를 작성합니다.
def test_add():
    """add 함수의 기본적인 경우들을 테스트합니다."""
    # assert 뒤의 조건이 참(True)이면 테스트를 통과합니다.
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """subtract 함수의 기본적인 경우들을 테스트합니다."""
    assert subtract(10, 5) == 5
    assert subtract(5, 5) == 0
```

파일 작성이 완료되면, 폴더 구조는 다음과 같습니다.
```
my-first-test/
├── .venv/
├── math_functions.py  <- 테스트 대상
├── test_math.py       <- 테스트 코드
└── pyproject.toml
```
이 구조는 실제 파이썬 프로젝트의 매우 일반적인 모습입니다.

#### `pytest`의 약속 (Convention over Configuration)

다시 한번 강조하지만, `pytest`가 이 파일들을 테스트로 인식하는 이유는 우리가 약속을 지켰기 때문입니다.
-   파일 이름이 `test_*.py` 형식입니다. (`test_math.py`)
-   테스트 함수 이름이 `test_` 로 시작합니다. (`def test_add():`)

### 3단계: 드디어, 테스트 실행!

모든 준비가 끝났습니다. 터미널이 `my-first-test` 디렉토리를 가리키고 있는지 확인한 후, 다음 명령어를 실행하세요.

```bash
uv run pytest
```
-   `uv run pytest`는 `.venv` 가상 환경 안에서 `pytest`를 실행하라는 명령어입니다.

### 4단계: 결과 확인

명령어를 실행하면, `pytest`가 현재 폴더와 하위 폴더를 탐색하여 약속에 맞는 테스트를 찾아 실행하고, 그 결과를 터미널에 보여줍니다.

```
============================= test session starts ==============================
...
collected 2 items

test_math.py ..                                                        [100%]

============================== 2 passed in ...s ===============================
```
-   `collected 2 items`: 2개의 테스트 함수를 찾았습니다.
-   `test_math.py ..`: `test_math.py` 파일의 테스트 2개가 모두 성공했습니다. (성공은 `.`)
-   `2 passed`: 최종적으로 2개의 테스트가 통과했습니다.

축하합니다! 여러분은 방금 실제 개발 과정과 거의 동일한 방식으로 여러분의 첫 번째 자동화된 테스트를 성공적으로 작성하고 실행했습니다.

---
**다음 세션**: [03. pytest 결과 해석하기](../03-interpreting-results/README.md)
