# 01. 모킹(Mocking)을 통한 테스트 독립성 확보

지금까지 우리가 테스트한 함수들은 모두 우리 코드 안에서만 동작하는 순수한(pure) 함수들이었습니다. 하지만 실제 애플리케이션은 외부 세계와 상호작용하는 경우가 훨씬 많습니다.
-   외부 API에 HTTP 요청을 보냅니다.
-   데이터베이스에 데이터를 읽고 씁니다.
-   파일 시스템에서 파일을 생성하거나 읽습니다.

이러한 **외부 의존성**이 있는 코드를 테스트하는 것은 매우 까다롭습니다. 왜냐하면,
-   **느립니다**: 실제 네트워크 요청이나 데이터베이스 접근은 많은 시간을 소요합니다.
-   **불안정합니다**: 네트워크가 끊기거나, 외부 API 서버가 다운되면 우리 코드와 상관없이 테스트가 실패합니다.
-   **비용이 듭니다**: 외부 유료 API의 경우, 테스트를 실행할 때마다 비용이 발생할 수 있습니다.
-   **통제가 불가능합니다**: 외부 API가 특정 시점에 특정 데이터를 반환하도록 우리가 제어할 수 없습니다.

**모킹(Mocking)**은 이러한 외부 의존성을 **'가짜 객체(Mock Object)'**로 대체하는 기술입니다. 가짜 객체는 실제 객체인 척 행동하며, 우리가 원하는 대로 미리 정해진 결과를 반환하거나 특정 예외를 발생시키도록 조종할 수 있습니다. 이를 통해 우리는 외부 세계로부터 우리의 코드를 완벽하게 **'격리(isolate)'**하여, 오직 우리 코드의 로직 자체에만 집중하여 빠르고 안정적으로 테스트할 수 있습니다.

### 실습: `requests` API 호출 모킹하기

이번 실습에서는 `pytest-mock` 플러그인을 사용하여, 외부 API에 HTTP 요청을 보내는 `requests` 라이브러리의 동작을 모킹해보겠습니다.

**1. 실습 환경 및 파일 준비**
`week2/04-advanced-pytest/01-mocking-with-pytest-mock/` 폴더에서 `my-mock-test`와 같은 실습 폴더를 만들고 `uv` 환경을 설정해주세요.

`pytest-mock` 플러그인은 `pytest`와 별도로 설치해야 합니다.
```bash
uv add --dev pytest pytest-mock
```
그 다음, `examples` 폴더의 `api_client.py`와 `test_api_client.py` 내용을 참고하여 `my-mock-test` 폴더 안에 동일한 파일들을 생성합니다.

**`api_client.py` (테스트 대상)**
```python
import requests

def get_user_email(user_id: int) -> str | None:
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        user_data = response.json()
        return user_data.get('email')
    except requests.exceptions.RequestException:
        return None
```

**`test_api_client.py` (모킹을 사용한 테스트)**
```python
from unittest.mock import Mock
from requests.exceptions import RequestException
from api_client import get_user_email

def test_get_user_email_success(mocker):
    # --- 준비 (Arrange) ---
    mock_response_data = {'email': 'Sincere@april.biz'}
    mock_get = mocker.patch('api_client.requests.get')
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_response_data
    mock_get.return_value.raise_for_status.return_value = None

    # --- 실행 (Act) ---
    user_email = get_user_email(1)

    # --- 단언 (Assert) ---
    assert user_email == 'Sincere@april.biz'
    mock_get.assert_called_once_with(
        'https://jsonplaceholder.typicode.com/users/1', 
        timeout=5
    )

def test_get_user_email_network_error(mocker):
    # --- 준비 (Arrange) ---
    mocker.patch(
        'api_client.requests.get', 
        side_effect=RequestException("Test network error")
    )

    # --- 실행 (Act) ---
    user_email = get_user_email(99)

    # --- 단언 (Assert) ---
    assert user_email is None
```

**2. 코드 심층 분석: `mocker.patch`의 마법**
`mocker`는 `pytest-mock`이 제공하는 Fixture입니다. 이 Fixture의 `patch` 기능이 모킹의 핵심입니다.

`mocker.patch('api_client.requests.get')`
-   이 코드는 `'api_client'` 모듈 안에서 사용되는 `requests.get`의 주소를 찾아, 그 자리를 우리가 조종할 수 있는 **가짜 Mock 객체로 임시로 바꿔치기**합니다.
-   **중요**: `patch`의 대상은 `requests.get`이 **'사용되는 곳'**(`api_client`)이지, 원본(`requests`)이 아닙니다.

`mock_get.return_value = ...`
-   바꿔치기한 가짜 객체가 호출되었을 때 무엇을 반환할지 설정합니다.
-   `requests.get`은 `Response` 객체를 반환하므로, 우리도 `.json()` 메서드를 가진 가짜 `Mock` 객체를 만들어 반환하도록 설정했습니다.

`side_effect=RequestException(...)`
-   `return_value` 대신 `side_effect`를 사용하면, 가짜 객체가 호출되었을 때 특정 값을 반환하는 대신 **예외(Exception)를 발생**시킬 수 있습니다. 이를 통해 우리는 네트워크 에러와 같은 예외 상황에 대해 우리 코드가 올바르게 대처하는지 테스트할 수 있습니다.

`mock_get.assert_called_once_with(...)`
-   Mock 객체는 자신이 어떻게 사용되었는지 모두 기억합니다. 테스트가 끝난 후, 우리는 Mock 객체를 통해 "네가 정확히 한 번만, 그리고 정확히 이 인자들로 호출되었니?"라고 검증할 수 있습니다. 이는 우리 코드가 올바른 URL과 파라미터로 외부 API를 호출하려고 했는지 보장하는 매우 중요한 검증 단계입니다.

**3. 테스트 실행**
`my-mock-test` 폴더에서 `uv run pytest`를 실행하면, 실제 네트워크 요청 없이도 모든 테스트가 1초도 안되어 성공적으로 통과하는 것을 확인할 수 있습니다.

모킹은 외부 의존성을 가진 복잡한 시스템을 테스트 가능하게 만드는 필수적인 기술입니다. 처음에는 조금 복잡해 보일 수 있지만, 그 원리를 이해하고 나면 단위 테스트의 품질과 범위를 획기적으로 높일 수 있게 될 것입니다.

---
**다음 세션**: [02. 코드 커버리지 소개 (pytest-cov)](../02-code-coverage-with-pytest-cov/README.md)
