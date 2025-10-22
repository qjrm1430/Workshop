# math_functions.py


def add(a, b):
    """두 숫자를 더한 값을 반환합니다."""
    return a + b


def divide(a, b):
    """한 숫자를 다른 숫자로 나눈 값을 반환합니다. 0으로 나눌 경우 예외가 발생합니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
