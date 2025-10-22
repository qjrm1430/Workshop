# pytest는 특별한 import나 클래스 상속이 필요 없습니다.

# 테스트 함수는 'test_'로 시작하면 됩니다.
def test_add():
    # 파이썬의 기본 'assert' 문을 사용합니다.
    assert 2 + 3 == 5
    assert -1 + 1 == 0


def test_subtract():
    assert 10 - 5 == 5
    assert 5 - 5 == 0
