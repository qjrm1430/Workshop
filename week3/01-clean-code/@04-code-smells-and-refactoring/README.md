# 03. 코드 스멜 & 리팩토링: 악취를 찾고 없애는 법

코드 스멜(Code Smell)은 **버그는 아니지만, 유지보수와 확장을 어렵게 만드는 구조적 문제**를 말합니다. 스멜을 발견하면 작은 리팩토링으로 개선해 나갑니다.

## 대표적 코드 스멜
- **긴 함수(Long Method)**: 많은 일을 하며 문맥 전환이 잦음 → 작은 함수로 분해
- **거대한 클래스(Large Class)**: 관련 없는 책임들이 혼재 → SRP로 분할
- **중복 코드(Duplicated Code)**: 로직 복붙 → 공통 함수/유틸로 추출
- **모호한 이름(Poor Naming)**: 목적이 불분명 → 역할을 드러내는 이름으로 변경
- **과도한 조건문(Deep Nesting)**: 중첩 if/else → 가드절, 다형성 활용
- **전역 상태(Global State)**: 숨은 의존성 → 주입/명시적 인자 전달

## 리팩토링 테크닉 (파이썬 중심)
- **함수 추출(Extract Function)**: 긴 함수를 작은 단위로 분리
- **클래스 추출(Extract Class)**: 거대한 클래스를 책임별로 분리
- **변수/함수/클래스 Rename**: 의미가 드러나도록 이름 개선
- **가드절로 전환**: 중첩 제거
- **의존성 주입(Dependency Injection)**: 전역/구체 의존 제거, 테스트 용이성 향상

### 예시: 과도한 조건문 제거
```python
# before
if status == "pending":
    handle_pending()
elif status == "approved":
    handle_approved()
elif status == "rejected":
    handle_rejected()
else:
    raise ValueError("unknown")

# after: 다형성 딕셔너리 매핑
handlers = {
    "pending": handle_pending,
    "approved": handle_approved,
    "rejected": handle_rejected,
}
handlers.get(status, lambda: (_ for _ in ()).throw(ValueError("unknown")))()
```

### 예시: 함수 추출로 테스트 가능성 개선
```python
# before

def process(values):
    # 정제
    values = [v.strip() for v in values if v]
    # 필터
    values = [v for v in values if v.isalpha()]
    # 출력
    print(",".join(values))

# after

def clean(values):
    return [v.strip() for v in values if v]

def filter_words(values):
    return [v for v in values if v.isalpha()]

def to_csv(values):
    return ",".join(values)

# 조합
print(to_csv(filter_words(clean(values))))
```

스멜 제거는 **작게, 안전하게, 테스트로 확인**하는 습관이 중요합니다. 오늘 한 줄의 리팩토링이 내일의 대형 문제를 막습니다.
