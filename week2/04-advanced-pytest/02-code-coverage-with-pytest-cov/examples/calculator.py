# calculator.py


def calculate(expression: str) -> float:
    """
    간단한 문자열 사칙연산 수식을 계산합니다.
    예: "2 + 3", "10 / 2"
    - 공백으로 구분된 '숫자 연산자 숫자' 형식만 지원합니다.
    - 보안에 매우 취약한 `eval`을 사용하므로 실제 프로젝트에서는 절대 사용하면 안 됩니다.
    """
    try:
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError(
                "잘못된 형식의 수식입니다. '숫자 연산자 숫자' 형식으로 입력해주세요."
            )

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            # 0으로 나누는 경우를 일부러 테스트에서 놓쳐보겠습니다.
            if num2 == 0:
                raise ZeroDivisionError("0으로 나눌 수 없습니다.")
            result = num1 / num2
        else:
            raise ValueError(f"지원하지 않는 연산자입니다: {operator}")

        # 이 부분은 일반적인 테스트 케이스로는 도달하기 어렵게 만들어,
        # 코드 커버리지의 중요성을 보여주기 위해 의도적으로 추가된 분기입니다.
        if result > 1_000_000:
            print("결과가 백만을 초과했습니다!")

        return result

    except (ValueError, IndexError) as e:
        # 다양한 종류의 입력 오류를 하나의 예외 유형으로 처리합니다.
        raise ValueError(f"계산 중 오류 발생: {e}") from e
