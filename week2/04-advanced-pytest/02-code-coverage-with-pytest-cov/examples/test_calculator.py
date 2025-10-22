# test_calculator.py
import pytest
from calculator import calculate


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2 + 3", 5.0),
        ("10 - 4", 6.0),
        ("5 * 8", 40.0),
        ("20 / 5", 4.0),
        ("-1 + 5", 4.0),
        ("3.14 * 2", 6.28),
    ],
)
def test_calculate_basic_operations(expression, expected):
    """기본적인 사칙연산이 정상적으로 수행되는지 테스트합니다."""
    assert calculate(expression) == expected


def test_calculate_invalid_expression():
    """잘못된 형식의 수식이 들어왔을 때 ValueError가 발생하는지 테스트합니다."""
    with pytest.raises(ValueError):
        calculate("2 +")


def test_calculate_unsupported_operator():
    """지원하지 않는 연산자가 들어왔을 때 ValueError가 발생하는지 테스트합니다."""
    with pytest.raises(ValueError, match="지원하지 않는 연산자입니다: %"):
        calculate("10 % 3")


# 의도적으로 누락된 테스트 케이스들:
# 1. 0으로 나누는 경우 (ZeroDivisionError)
# 2. 결과값이 백만을 초과하는 경우
