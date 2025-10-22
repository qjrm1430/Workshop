# test_api_simulation.py
import sys
import time

import pytest

# === 테스트 대상 함수 시뮬레이션 ===
# 실제 API 호출 대신, 호출에 시간이 걸리는 것처럼 흉내 내는 함수들입니다.


def get_user_profile(user_id):
    """사용자 프로필을 가져오는 API (시간이 오래 걸리는 작업 시뮬레이션)"""
    print(f"\n>> {user_id}번 사용자 프로필 API 호출 시작...")
    time.sleep(1)
    print(">> API 응답 받음")
    return {"id": user_id, "name": "Alice", "email": "alice@example.com"}


def get_articles(user_id):
    """사용자가 작성한 게시글 목록을 가져오는 API (아직 개발 중인 기능)"""
    # 이 기능은 아직 구현되지 않았다고 가정합니다.
    raise NotImplementedError("게시글 API는 아직 개발 중입니다.")


def get_system_status():
    """시스템 상태를 확인하는 API (Python 3.10 이상에서만 제대로 동작)"""
    if sys.version_info < (3, 10):
        # 구 버전을 위한 임시 반환 값 (약간의 버그가 있음)
        return {"status": "ok", "version": "legacy"}
    return {"status": "ok", "version": "3.10+"}


# === 테스트 코드 ===


@pytest.mark.slow
def test_get_user_profile():
    """느린 테스트: 사용자 프로필 API가 정상 동작하는지 테스트합니다."""
    print("test_get_user_profile 실행")
    profile = get_user_profile(1)
    assert profile["id"] == 1
    assert profile["name"] == "Alice"


@pytest.mark.skip(reason="현재 게시글 API는 미구현 상태이므로 이 테스트를 건너뜁니다.")
def test_get_articles():
    """건너뛰는 테스트: 미구현된 게시글 API를 테스트합니다."""
    print("test_get_articles 실행")
    articles = get_articles(1)
    assert isinstance(articles, list)


@pytest.mark.skipif(
    sys.version_info >= (3, 10),
    reason="Python 3.10 이상에서는 이 레거시 테스트가 불필요합니다.",
)
def test_get_system_status_legacy():
    """조건부 건너뛰기: Python 3.10 미만에서만 실행되는 레거시 시스템 상태 테스트"""
    print("test_get_system_status_legacy 실행")
    status = get_system_status()
    assert status["version"] == "legacy"


@pytest.mark.xfail(
    sys.version_info < (3, 10),
    reason="Python 3.10 미만에서는 이 기능에 약간의 버그가 있습니다.",
)
def test_get_system_status_modern():
    """예상된 실패: 최신 시스템 상태 API의 동작을 테스트합니다."""
    print("test_get_system_status_modern 실행")
    status = get_system_status()
    # Python 3.10 미만에서는 status['version']이 'legacy'이므로 이 assert는 실패할 것입니다.
    # 하지만 xfail 마커 덕분에 테스트 실행은 중단되지 않습니다.
    assert status["version"] == "3.10+"
