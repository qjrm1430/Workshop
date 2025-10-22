# 03. 마커를 이용한 테스트 스위트 구성 및 실행 전략

프로젝트가 커지고 테스트의 개수가 수백, 수천 개로 늘어나면 모든 테스트를 한 번에 실행하는 것이 비효율적이거나 불가능해질 수 있습니다. 어떤 테스트는 1초도 안 걸리지만, 어떤 테스트는 실제 네트워크나 데이터베이스에 접근하느라 수십 초가 걸릴 수도 있기 때문입니다.

`pytest`의 **마커(Marker)**는 각 테스트 함수에 **'꼬리표'**를 붙이는 기능입니다. 이 꼬리표를 이용해 우리는 테스트를 그룹화하고, 특정 그룹의 테스트만 선택적으로 실행하거나 제외하는 등 테스트 실행 과정을 자유롭게 제어할 수 있습니다.

### 마커는 언제, 왜 사용해야 할까요?

-   **속도 제어**: 빠르게 실행되는 '단위 테스트' 그룹과, 느리게 실행되는 '통합 테스트' 또는 'E2E 테스트' 그룹을 분리하여 실행하고 싶을 때.
-   **환경 제어**: 특정 운영체제나 파이썬 버전에서만 실행되어야 하는 테스트를 표시할 때.
-   **상태 관리**: 아직 구현되지 않았거나, 현재 알려진 버그로 인해 실패하는 테스트를 명시적으로 관리하고 싶을 때.
-   **기능 그룹화**: '인증 관련 테스트', '결제 관련 테스트' 등 기능 단위로 테스트를 묶어 관리하고 싶을 때.

### 실습: 다양한 마커 직접 사용해보기

이번 실습에서는 `pytest`에 내장된 기본 마커들과 우리가 직접 만드는 커스텀 마커를 모두 사용해보며 그 차이와 활용법을 익혀보겠습니다.

**1. 실습 환경 및 파일 준비**
`week2/03-pytest-core-features/03-markers/` 폴더에서 `my-marker-test`와 같은 실습 폴더를 만들고 `uv` 환경을 설정해주세요.

그 다음, `examples` 폴더의 `test_api_simulation.py`와 `pytest.ini` 내용을 참고하여 `my-marker-test` 폴더 안에 동일한 파일들을 생성합니다.

**`test_api_simulation.py` (다양한 마커가 적용된 테스트)**
```python
import pytest
import time
import sys
# ... (시뮬레이션 함수 생략) ...

# 1. 사용자 정의 마커
@pytest.mark.slow
def test_get_user_profile():
    # ... (1초 대기) ...

# 2. 내장 마커: 무조건 건너뛰기
@pytest.mark.skip(reason="API 미구현")
def test_get_articles():
    # ...

# 3. 내장 마커: 조건부 건너뛰기
@pytest.mark.skipif(sys.version_info >= (3, 10), reason="Py 3.10+ 불필요")
def test_get_system_status_legacy():
    # ...

# 4. 내장 마커: 예상된 실패
@pytest.mark.xfail(sys.version_info < (3, 10), reason="Py 3.10 미만 버그")
def test_get_system_status_modern():
    # ...
```

**`pytest.ini` (사용자 정의 마커 등록)**
```ini
[pytest]
markers =
    slow: marks tests as slow to run
```
> **중요**: `pytest.ini` 파일에 커스텀 마커를 등록해주어야 `pytest`가 해당 마커를 공식적으로 인식하고, 실행 시 불필요한 경고 메시지를 보여주지 않습니다.

**2. 테스트 실행 및 분석**

터미널에서 다양한 `-m` 옵션을 사용하여 테스트를 선택적으로 실행해봅시다.

**A) 전체 테스트 실행 (`uv run pytest -v`)**
-   `test_get_user_profile`: 1초가 걸리며 `PASSED`
-   `test_get_articles`: `SKIPPED (s)`
-   `test_get_system_status_legacy`: `SKIPPED (s)` 또는 `PASSED` (파이썬 버전에 따라 다름)
-   `test_get_system_status_modern`: `XFAIL (x)` 또는 `PASSED` (파이썬 버전에 따라 다름)

**B) `@slow` 마커가 붙은 테스트만 실행 (`uv run pytest -v -m slow`)**
-   `test_get_user_profile` 테스트만 실행되고, 1초의 실행 시간이 걸리는 것을 확인할 수 있습니다.

**C) `@slow` 마커가 붙은 테스트는 제외하고 실행 (`uv run pytest -v -m "not slow"`)**
-   `test_get_user_profile`을 제외한 나머지 테스트들만 거의 즉시 실행됩니다.

이처럼 `-m` 옵션을 사용하면 빠르고 가벼운 단위 테스트들은 커밋할 때마다 실행하여 즉각적인 피드백을 얻고, 시간이 오래 걸리는 테스트들은 야간 빌드나 CI/CD의 특정 단계에서만 실행하는 등 매우 효율적인 테스트 전략을 수립할 수 있습니다.

마커는 단순한 분류 도구를 넘어, 대규모 프로젝트의 테스트 스위트를 현실적으로 관리하고 자동화 파이프라인의 효율을 극대화하는 전략적인 핵심 기능입니다.

---
**다음 파트**: [Part 4. '어디서' 활용하는가: 고급 및 실제 적용 기술](../../04-advanced-pytest/01-mocking-with-pytest-mock/README.md)
