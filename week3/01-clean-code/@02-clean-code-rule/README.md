## 왜 이렇게 이름을 지어야 하는가

좋은 이름은 **코드의 의도**를 즉시 드러내어, 이해와 변경을 빠르게 합니다. 팀 개발에서는 이름이 곧 커뮤니케이션 도구입니다.

- **가독성 향상**: 의미가 선명한 이름은 주석 없이도 무슨 일을 하는지 파악하게 합니다.
- **인지 부하 감소**: 모호한 약어/축약 대신 명확한 단어를 사용하면 코드를 해석하는 정신적 비용이 줄어듭니다.
- **검색/탐색 용이**: 일관된 네이밍 규칙은 코드베이스를 빠르게 찾고 이동하게 합니다(에디터/grep 검색).
- **온보딩 속도 증가**: 새 팀원이 규칙적인 이름만으로 구조와 책임을 쉽게 이해합니다.
- **테스트/리뷰 효율**: 이름만 보고 예상되는 동작을 추론할 수 있어 테스트 시나리오/리뷰 포인트가 명확해집니다.
- **리팩토링 안전성**: 책임이 드러난 이름은 책임 분리와 구조 개선을 자연스럽게 이끕니다.

## Naming Rule

### 1. 변수/클래스명: 명사(Noun)

```python
# Bad
class FeatureExtract:
    pass
work = 10

# Good
class FeatureExtractor:
    pass
worker_count = 10
```

### 2. 관사(the/a) 생략, 전치사는 간결하게

```python
# Bad
a_cat = "Tom"
the_number_of_worker = 12

# Good
cat = "Tom"
num_workers = 12

# 이름 내 약어/숫자 결합은 일관성 유지
class Seq2Seq:
    pass

def sentence_to_id(sentence: str) -> list[int]:
    # ...
    return []

char2id: dict[str, int] = {}
```

### 3. 반복자: 단수/복수 구분 명확히

```python
items = [1, 2, 3, 4, 5]

for item in items:
    print(item)
```

### 4. 함수명: 동사+명사 (행동을 드러내기)

```python
# Bad
def id():
    return 42

# Good
def get_id() -> int:
    return 42
```

### 5. Boolean 변수: is_, has_, can_ 접두사

```python
is_human = True
is_animal = False
is_exist = True
is_final_data = False
has_permission = True
can_execute = False
```

## 가독성 향상 Rule

### 주석은 설명하려는 구문에 맞춰 들여쓰기

```python
def some_function() -> None:
    total = 0

    # 누적 합을 계산한다
    for i in range(10):
        total += i

    # 결과를 출력한다
    print(total)
```

### 연산자 사이에 공백 추가

```python
# Bad
a+b+c+d

# Good
a + b + c + d
```

### 콤마 뒤에는 공백 추가

```python
# Bad
arr = [1,2,3,4]

# Good
arr = [1, 2, 3, 4]
```

### 괄호로 묶어 자연스러운 줄바꿈

```python
result = some_function(
    very_long_argument,
    another_long_argument,
    yet_another_argument,
)
```

### 네이밍은 역할을 드러내도록

```python
# Bad
x = [1, 2, 3]

def f(l):
    return sum(l)

# Good
numbers = [1, 2, 3]

def sum_numbers(values: list[int]) -> int:
    return sum(values)
```

### 불필요한 축약/약어 지양, 팀 합의된 약어만 사용

```python
# Bad
cfg = load()
usr = get_user()

# Good
config = load()
user = get_user()
```