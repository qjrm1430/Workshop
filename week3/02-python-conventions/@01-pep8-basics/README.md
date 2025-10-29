# 01. PEP 8 기초: 파이썬 스타일 가이드 핵심

PEP 8은 파이썬 코드의 **일관성과 가독성**을 높이기 위한 스타일 가이드입니다. 팀의 합의를 우선하되, 기본은 PEP 8을 따릅니다.

## 핵심 규칙 요약
- **들여쓰기**: 공백 4칸 (탭 금지)
- **라인 길이**: 88자 권장 (Ruff/Black과 호환)
- **네이밍**:
  - 변수/함수: `snake_case`
  - 클래스: `PascalCase`
  - 상수: `UPPER_SNAKE_CASE`
- **Imports**:
  - 표준 라이브러리 → 서드파티 → 로컬 패키지 순
  - 한 줄 한 모듈, 필요 시 as alias
- **공백**:
  - 괄호 안/콤마 뒤에는 공백, 함수 호출의 `()` 앞에는 공백 없음

## 예시
```python
# bad
import os,sys
class user:
    pass

def add (a, b): return a+b

# good
import os
import sys

class User:
    pass

def add(a: int, b: int) -> int:
    return a + b
```

라인이 길어지면 괄호로 묶어 자연스럽게 줄바꿈합니다.
```python
result = some_function(
    very_long_argument,
    another_long_argument,
    yet_another_argument,
)
```
