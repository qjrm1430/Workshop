# test_math_issues.py

from math_functions import add, divide


def test_add_failure():
    """
    이 테스트는 코드의 '로직'이 틀렸을 때 발생하는 '실패(Failure)' 상황을 보여줍니다.
    기능은 정상적으로 실행되었지만, 그 결과가 우리의 기대와 다릅니다.
    """
    # 2 + 2의 결과는 4이지만, 일부러 5라고 기대하여 '실패'를 유도합니다.
    assert add(2, 2) == 5


def test_divide_error():
    """
    이 테스트는 코드를 실행하는 도중 예기치 않은 예외가 발생했을 때의 '오류(Error)' 상황을 보여줍니다.
    assert 문에 도달하기도 전에 테스트가 비정상적으로 중단됩니다.
    """
    # 0으로 나누면 ValueError가 발생하여 '오류'가 납니다.
    divide(10, 0)
