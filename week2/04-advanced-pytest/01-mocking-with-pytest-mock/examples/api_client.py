# api_client.py
import requests


def get_json_from_url(url: str) -> dict:
    """
    주어진 URL에 GET 요청을 보내고, 응답받은 JSON을 파싱하여 딕셔너리로 반환합니다.
    - 요청이 실패하거나 응답이 JSON이 아닐 경우 예외가 발생할 수 있습니다.
    - 이 함수는 실제 네트워크에 의존하기 때문에 테스트하기 까다롭습니다.
    """
    try:
        response = requests.get(url, timeout=5)
        # HTTP 에러 (4xx, 5xx)가 발생하면 예외를 일으킵니다.
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"네트워크 오류 발생: {e}")
        raise


def get_user_email(user_id: int) -> str | None:
    """
    사용자 ID를 받아와 외부 서비스에서 사용자 이메일을 조회합니다.
    """
    # jsonplaceholder는 테스트용 가짜 API를 제공하는 온라인 서비스입니다.
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        user_data = get_json_from_url(api_url)
        return user_data.get("email")
    except requests.exceptions.RequestException:
        # get_json_from_url에서 발생한 예외를 처리합니다.
        return None
