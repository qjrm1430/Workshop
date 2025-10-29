# 01. 클린 코드란 무엇인가: 읽기 쉬운 코드가 왜 승리하는가

클린 코드(Clean Code)는 **읽기 쉽고, 이해하기 쉬우며, 수정하기 쉬운 코드**를 의미합니다. 빠르게 동작하는 '작동하는 코드'만으로는 충분하지 않습니다. **시간이 지나도 팀이 자신 있게 바꿀 수 있는 코드**가 좋은 코드입니다.

### 왜 클린 코드가 중요한가?
- **가독성(Readability)**: 코드는 '한 번 쓰고 여러 번 읽는' 산출물입니다. 팀원(미래의 나 포함)이 빠르게 이해할 수 있어야 합니다.
- **유지보수성(Maintainability)**: 요구사항 변경이 일어날 때, 부작용 없이 안전하게 수정할 수 있어야 합니다.
- **확장성(Extensibility)**: 새로운 기능을 추가할 때 기존 코드 구조가 이를 자연스럽게 받아들일 수 있어야 합니다.
- **테스트 용이성(Testability)**: 작고 분리된 단위는 테스트하기 쉬우며, 테스트 가능한 설계는 클린 코드의 결과이자 촉진제입니다.

### 클린 코드의 핵심 원칙 (요약)
- **명확한 이름 짓기**: 변수/함수/클래스의 목적이 이름만으로 충분히 드러나야 합니다.
- **작은 함수**: 함수는 작게, 하나의 일을 잘하게. 인자 수를 줄이고 부작용을 피합니다.
- **단일 책임(SRP)**: 하나의 모듈은 하나의 변경 이유만 가져야 합니다.
- **의존성 최소화**: 낮은 결합도와 높은 응집도를 지향합니다.
- **중복 제거(DRY)**: 중복된 로직을 제거하고, 공통화하여 한 곳에서 관리합니다.

### 나쁜 코드 → 좋은 코드 (간단 예시)

```python
# 나쁜 예: 이름이 모호하고 여러 책임이 섞여 있음

def handle(d, t):
    # 데이터 정제
    r = []
    for i in d:
        if i and i != "":
            r.append(i.strip())
    # 필터링
    if t == "number":
        r = [x for x in r if x.isdigit()]
    elif t == "word":
        r = [x for x in r if x.isalpha()]
    # 출력
    print(",".join(r))

# 좋은 예: 이름이 명확하고, 작은 함수로 책임 분리

def clean(values: list[str]) -> list[str]:
    return [v.strip() for v in values if v]


def filter_by_type(values: list[str], kind: str) -> list[str]:
    if kind == "number":
        return [v for v in values if v.isdigit()]
    if kind == "word":
        return [v for v in values if v.isalpha()]
    raise ValueError("kind must be 'number' or 'word'")


def print_csv(values: list[str]) -> None:
    print(",".join(values))


def main(values: list[str], kind: str) -> None:
    cleaned = clean(values)
    filtered = filter_by_type(cleaned, kind)
    print_csv(filtered)
```
- 나쁜 예에서는 가독성이 떨어지고, 테스트가 어려우며, 요구사항 추가(예: `kind='alnum'`) 시 함수 전체를 수정해야 합니다.
- 좋은 예에서는 각 함수가 한 가지 책임만 가지며, 테스트와 변경이 쉬워집니다.

---
**다음 세션**: [02. SOLID 원칙](../@02-principles-solid/README.md)
