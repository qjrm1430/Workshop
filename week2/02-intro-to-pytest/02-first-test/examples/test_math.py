# test_math.py

# 테스트 대상 함수들을 math_functions.py 파일로부터 가져옵니다.
from math_functions import add, subtract


# 'test_'로 시작하는 함수를 만들어 테스트를 작성합니다.
def test_add():
    """add 함수의 기본적인 경우들을 테스트합니다."""
    # assert 뒤의 조건이 참(True)이면 테스트를 통과합니다.
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10
    assert add(0, 0) == 0


def test_subtract():
    """subtract 함수의 기본적인 경우들을 테스트합니다."""
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(5, 5) == 0
