# test_math.py

from math_functions import add, subtract


# 테스트 함수는 반드시 'test_'로 시작해야 합니다.
def test_add():
    """add 함수의 기본 기능을 테스트합니다."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10


def test_subtract():
    """subtract 함수의 기본 기능을 테스트합니다."""
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(5, 5) == 0


# 결과를 해석하는 방법을 배우기 위해 의도적으로 실패하는 테스트를 추가합니다.
def test_add_failing():
    """add 함수에 대한 실패 케이스를 테스트합니다."""
    # 2 + 2는 4이지만, 일부러 5라고 기대하여 실패를 유도합니다.
    assert add(2, 2) == 5
