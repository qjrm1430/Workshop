# test_api_client.py
from unittest.mock import Mock

# 테스트 대상 모듈을 import 합니다.
from api_client import get_user_email
from requests.exceptions import RequestException


def test_get_user_email_success(mocker):
    """
    API 호출이 성공했을 경우, 이메일을 정상적으로 반환하는지 테스트합니다.
    """
    # --- 준비 (Arrange) ---
    # 1. 가짜 응답 객체를 만듭니다. 실제 API 응답과 유사한 구조를 가집니다.
    mock_response_data = {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz",
    }

    # 2. `mocker.patch`를 사용하여 'api_client.requests.get'의 동작을 가로챕니다.
    #    이제 테스트 중에 `api_client` 모듈 내에서 `requests.get`이 호출되면
    #    실제 네트워크 요청 대신 우리가 정의한 가짜 객체가 사용됩니다.
    mock_get = mocker.patch("api_client.requests.get")

    # 3. 가짜 `requests.get`이 반환할 객체를 설정합니다.
    #    - `return_value`는 `requests.get`의 반환값인 Response 객체를 흉내 냅니다.
    #    - 이 가짜 Response 객체는 `.json()` 메서드를 가지고 있어야 합니다.
    #    - `.json()` 메서드는 호출 시 `mock_response_data`를 반환하도록 설정합니다.
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_response_data
    # `raise_for_status`는 호출 시 아무 일도 하지 않도록 설정합니다 (성공 상황이므로).
    mock_get.return_value.raise_for_status.return_value = None

    # --- 실행 (Act) ---
    user_email = get_user_email(1)

    # --- 단언 (Assert) ---
    # 1. 반환된 이메일이 우리가 설정한 가짜 데이터와 일치하는지 확인합니다.
    assert user_email == "Sincere@april.biz"

    # 2. `requests.get`이 정확히 어떤 URL로 호출되었는지 검증합니다.
    #    이를 통해 우리 코드가 올바른 API 엔드포인트를 호출했는지 확신할 수 있습니다.
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/1", timeout=5
    )


def test_get_user_email_network_error(mocker):
    """
    네트워크 오류(RequestException)가 발생했을 경우, None을 반환하는지 테스트합니다.
    """
    # --- 준비 (Arrange) ---
    # `requests.get`이 호출될 때 `RequestException`을 발생시키도록 설정합니다.
    # `side_effect`는 함수 호출 시 반환값 대신 예외를 발생시킬 때 사용합니다.
    mock_get = mocker.patch(
        "api_client.requests.get", side_effect=RequestException("Test network error")
    )

    # --- 실행 (Act) ---
    user_email = get_user_email(99)

    # --- 단언 (Assert) ---
    # 네트워크 에러가 발생했으므로, 함수는 None을 반환해야 합니다.
    assert user_email is None

    # 이 경우에도 `requests.get`이 올바른 URL로 호출되었는지 확인할 수 있습니다.
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/99", timeout=5
    )
