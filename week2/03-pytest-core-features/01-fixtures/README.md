# 01. Fixture의 힘: 상태와 의존성 관리

이전 파트에서 우리는 간단한 함수들을 테스트했습니다. 하지만 실제 애플리케이션의 함수들은 대부분 혼자 동작하지 않습니다. 데이터베이스 연결이 필요하거나, 특정 파일을 읽어야 하거나, 네트워크 요청을 보내야 하는 등 다양한 **'준비물(의존성)'**이 필요한 경우가 많습니다.

테스트를 작성할 때, 각각의 테스트가 독립적이고 일관된 환경에서 실행되도록 이 '준비물'들을 관리하는 것은 매우 중요하고도 번거로운 일입니다. `pytest`의 **Fixture**는 바로 이 문제를 아주 우아하고 강력하게 해결해주는 기능입니다.

### Fixture란 무엇인가? - 단순한 '준비'를 넘어

Fixture는 테스트를 실행하기 전에 필요한 **모든 준비(Setup) 과정을 처리**하고, 테스트가 끝난 후에 **뒷정리(Teardown)를 보장**하는 재사용 가능한 함수입니다.

-   **준비 (Setup)**: 테스트에 필요한 객체 생성, 데이터베이스 연결, 테스트 데이터 초기화 등
-   **실행 (Yield)**: 준비된 '준비물'을 테스트 함수에 전달하여 테스트 실행
-   **정리 (Teardown)**: 사용한 리소스 해제 (예: 데이터베이스 연결 종료, 임시 파일 삭제)

이러한 `Setup -> Yield -> Teardown` 패턴은 테스트 코드의 중복을 극적으로 줄여주고, 각 테스트가 무엇에 의존하는지 명확하게 보여주며, 테스트의 안정성을 크게 높여줍니다.

### 실습: 데이터베이스 연결 관리하기

말로만 듣는 것보다 직접 경험하는 것이 가장 좋습니다. 이번 실습에서는 여러 테스트에서 공통으로 필요한 '데이터베이스 연결' 객체를 Fixture로 만들어 관리해보겠습니다.

**1. 실습 환경 준비**
`week2/03-pytest-core-features/01-fixtures/` 폴더로 이동한 후, 터미널에서 다음 명령을 실행하여 실습 환경을 만듭니다.

```bash
# 실습용 폴더 생성 및 이동
mkdir my-fixture-test
cd my-fixture-test

# uv 환경 초기화 및 pytest 설치
uv init
uv add --dev pytest
```

**2. 실습 파일 작성**
`my-fixture-test` 폴더 안에, 이 세션의 `examples` 폴더에 있는 `student_db.py`와 `test_student_db.py`의 내용을 참고하여 동일한 파일들을 생성해주세요.

**`student_db.py` (테스트 대상)**
```python
# student_db.py

class StudentDB:
    def __init__(self):
        self._data = {}

    def connect(self, db_name):
        print(f"'{db_name}' 데이터베이스에 연결합니다...")
        # 실제 DB 연결 대신 딕셔너리를 사용해 간단히 흉내 냅니다.
        self._data = {
            1: {'name': 'Alice', 'major': 'Computer Science'},
            2: {'name': 'Bob', 'major': 'Data Science'},
            3: {'name': 'Charlie', 'major': 'Mathematics'}
        }
        print("연결 성공.")

    def get_student_name(self, student_id):
        student = self._data.get(student_id)
        return student['name'] if student else None

    def close(self):
        print("데이터베이스 연결을 닫습니다...")
        self._data = {}
        print("연결 종료.")
```

**`test_student_db.py` (Fixture를 사용한 테스트)**
```python
# test_student_db.py
import pytest
from student_db import StudentDB

@pytest.fixture
def db():
    # --- 1. 설정 (Setup) ---
    print("\n--- Fixture: 설정 시작 ---")
    db_instance = StudentDB()
    db_instance.connect('test_db')
    
    # --- 2. 전달 (Yield) ---
    yield db_instance
    
    # --- 3. 정리 (Teardown) ---
    print("--- Fixture: 정리 시작 ---")
    db_instance.close()

def test_get_student_name_alice(db):
    print(">> test_get_student_name_alice 실행")
    student_name = db.get_student_name(1)
    assert student_name == 'Alice'

def test_get_student_name_bob(db):
    print(">> test_get_student_name_bob 실행")
    student_name = db.get_student_name(2)
    assert student_name == 'Bob'
```

**3. 테스트 실행 및 결과 분석**

`my-fixture-test` 폴더에서 `uv run pytest -v -s` 명령을 실행해봅시다.
- `-v` (verbose): 각 테스트의 이름을 자세히 보여줍니다.
- `-s`: 테스트 실행 중 `print`문의 출력을 보여줍니다.

**실행 결과:**
```
test_student_db.py::test_get_student_name_alice 
--- Fixture: 설정 시작 ---
'test_db' 데이터베이스에 연결합니다...
연결 성공.
>> test_get_student_name_alice 실행
PASSED
--- Fixture: 정리 시작 ---
데이터베이스 연결을 닫습니다...
연결 종료.

test_student_db.py::test_get_student_name_bob 
--- Fixture: 설정 시작 ---
'test_db' 데이터베이스에 연결합니다...
연결 성공.
>> test_get_student_name_bob 실행
PASSED
--- Fixture: 정리 시작 ---
데이터베이스 연결을 닫습니다...
연결 종료.
```

결과를 보면 놀라운 사실을 알 수 있습니다. **각각의 테스트 함수가 실행될 때마다 `db` Fixture가 독립적으로 호출되어 `설정`과 `정리` 과정을 반복**했다는 것입니다. 이 덕분에 각 테스트는 항상 깨끗하고 새로운 `db` 객체를 받아 서로에게 전혀 영향을 주지 않는, 완벽하게 독립적인 테스트가 될 수 있었습니다.

### Fixture의 범위(Scope): 현명한 리소스 관리

만약 DB 연결처럼 한 번 만드는 데 비용이 많이 드는 리소스를 모든 테스트마다 새로 만들고 싶지 않다면 어떻게 할까요? 이때 `scope` 매개변수를 사용합니다.

`@pytest.fixture(scope="module")`
-   `scope="function"` (기본값): Fixture가 테스트 함수마다 실행됩니다.
-   `scope="class"`: 클래스 단위로 한 번만 실행됩니다.
-   `scope="module"`: 테스트 파일(`*.py`) 단위로 한 번만 실행됩니다.
-   `scope="session"`: 전체 테스트 실행 시 단 한 번만 실행됩니다.

`test_student_db.py`의 Fixture를 `@pytest.fixture(scope="module")`로 바꾸고 다시 테스트를 실행해보세요. `설정`과 `정리`가 단 한 번만 실행되는 것을 확인할 수 있을 겁니다. 이처럼 `scope`를 사용하면 테스트의 독립성과 실행 속도 사이에서 최적의 균형점을 찾을 수 있습니다.

Fixture는 `pytest`를 다른 테스트 프레임워크와 차별화하는 가장 강력하고 핵심적인 기능입니다. 처음에는 조금 낯설 수 있지만, 일단 익숙해지면 여러분의 테스트 코드를 훨씬 더 깨끗하고, 효율적이며, 유지보수하기 쉽게 만들어 줄 것입니다.

---
**다음 세션**: [02. 파라미터화를 통한 데이터 주도 테스트](../02-parametrization/README.md)
