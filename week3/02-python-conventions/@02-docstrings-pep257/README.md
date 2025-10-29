# 02. Docstrings (PEP 257): 코드 자체를 설명하는 문서

Docstring은 모듈/클래스/함수의 **의도를 코드 옆에 남기는 문서**입니다. 도구(Ruff 등)가 이를 검사해 일관성을 유지할 수 있습니다.

## 기본 형식
```python
def add(a: int, b: int) -> int:
    """두 정수를 더한 값을 반환합니다.

    Args:
        a: 첫 번째 정수.
        b: 두 번째 정수.

    Returns:
        두 수의 합.
    """
    return a + b
```

- 첫 줄은 요약(한 문장), 그 다음 빈 줄 후 상세 설명.
- 파라미터/리턴/예외는 일관된 섹션명 사용(Google/NumPy 등 팀 합의).

## 클래스/모듈 Docstring
```python
class Order:
    """쇼핑 주문을 표현합니다.

    Attributes:
        id: 주문 ID.
        items: 주문 항목 목록.
    """
```

Docstring은 **테스트와 코드 리뷰**에서 큰 힘을 발휘합니다. 의도를 명확히 하여 오해를 줄입니다.
