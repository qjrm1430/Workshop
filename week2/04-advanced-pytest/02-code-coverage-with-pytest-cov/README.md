# 02. 안전망 측정: 코드 커버리지 소개 (pytest-cov)

우리는 지금까지 많은 테스트를 작성했습니다. 하지만 문득 이런 질문이 들 수 있습니다. "우리의 테스트가 얼마나 충분할까?", "혹시 우리가 놓치고 있는 중요한 코드 경로는 없을까?"

**코드 커버리지(Code Coverage)**는 우리가 작성한 테스트가 실제 프로덕션 코드의 몇 퍼센트를 실행했는지 측정하는 지표입니다. 이는 우리 테스트 스위트라는 '안전망'이 코드베이스의 얼마나 넓은 영역을 덮고 있는지 보여주는 객관적인 데이터입니다.

### 커버리지는 '진단 도구'이지, '성적표'가 아니다

초보 개발자들이 가장 흔하게 하는 오해는 코드 커버리지 수치를 맹목적인 목표로 삼는 것입니다. "무조건 100%를 달성해야 한다"는 생각은 종종 숫자만 높이기 위한 의미 없는 테스트를 양산하는 부작용을 낳습니다.

**커버리지의 진정한 가치**는 최종 퍼센트 수치가 아니라, **'어떤 코드가 테스트되지 않았는지(Missing)'를 정확히 알려주는 진단 기능**에 있습니다. 커버리지 리포트는 우리 테스트가 놓치고 있는 코드의 '사각지대'를 정확히 찾아주는 내비게이션과 같습니다.

### 실습: `pytest-cov`로 테스트의 빈틈 찾아내기

`pytest-cov`는 `pytest`와 완벽하게 통합되어 코드 커버리지를 쉽게 측정하게 해주는 플러그인입니다.

**1. 실습 환경 및 파일 준비**
`week2/04-advanced-pytest/02-code-coverage-with-pytest-cov/` 폴더에서 `my-coverage-test`와 같은 실습 폴더를 만들고 `uv` 환경을 설정해주세요.

`pytest-cov` 플러그인을 설치합니다.
```bash
uv add --dev pytest pytest-cov
```
그 다음, `examples` 폴더의 `calculator.py`와 `test_calculator.py` 내용을 참고하여 `my-coverage-test` 폴더 안에 동일한 파일들을 생성합니다.

**`calculator.py` (테스트 대상)**
```python
def calculate(expression: str) -> float:
    # ... (생략) ...
        elif operator == '/':
            # [!] 이 분기문은 테스트되지 않을 것입니다.
            if num2 == 0:
                raise ZeroDivisionError("0으로 나눌 수 없습니다.")
            result = num1 / num2
    # ... (생략) ...
        # [!] 이 분기문도 테스트되지 않을 것입니다.
        if result > 1_000_000:
            print("결과가 백만을 초과했습니다!")
    # ... (생략) ...
```

**`test_calculator.py` (불완전한 테스트)**
```python
# ... (생략) ...
# 의도적으로 누락된 테스트 케이스들:
# 1. 0으로 나누는 경우 (ZeroDivisionError)
# 2. 결과값이 백만을 초과하는 경우
```

**2. 커버리지 측정 실행**
터미널에서 다음 명령을 실행하여, `calculator.py` 파일을 대상으로 커버리지를 측정합니다.

```bash
uv run pytest --cov=calculator
```
-   `--cov=calculator`: 커버리지를 측정할 대상 모듈(파일)을 지정합니다.

**3. 커버리지 리포트 분석**

실행 결과로 다음과 같은 간단한 리포트가 터미널에 출력됩니다.

```
---------- coverage: platform win32, python 3.11.5 -----------
Name             Stmts   Miss  Cover
------------------------------------
calculator.py       22      4    82%
------------------------------------
TOTAL               22      4    82%
```
-   `Stmts`: 전체 실행 가능한 코드 라인 수 (22개)
-   `Miss`: 테스트에 의해 실행되지 않은 코드 라인 수 (4개)
-   `Cover`: 커버리지 비율 (82%)

82%는 나쁘지 않은 수치처럼 보이지만, 진짜 중요한 정보는 저 `Miss` 4줄에 있습니다. 어떤 라인이 누락되었는지 확인하려면, 다음 명령으로 HTML 리포트를 생성해봅시다.

```bash
uv run pytest --cov=calculator --cov-report=html
```
이 명령을 실행하면 현재 폴더에 `htmlcov/` 디렉토리가 생성됩니다. 그 안의 `index.html` 파일을 웹 브라우저로 열어보세요.

![Coverage HTML Report](https://i.imgur.com/your-image-link.png) <!-- 이미지 링크는 예시입니다 -->

`calculator.py`를 클릭하면, 테스트되지 않은 코드 라인이 빨간색으로 명확하게 표시되는 것을 볼 수 있습니다. 바로 `if num2 == 0:` 부분과 `if result > 1_000_000:` 부분입니다.

**4. 테스트 보강 및 커버리지 100% 달성**
이제 커버리지 리포트가 알려준 '사각지대'를 없애기 위해 `test_calculator.py`에 테스트 케이스를 추가합시다.

```python
# test_calculator.py에 추가

def test_calculate_division_by_zero():
    """0으로 나눌 때 ZeroDivisionError가 발생하는지 테스트합니다."""
    with pytest.raises(ZeroDivisionError):
        calculate("10 / 0")

def test_calculate_large_number_result():
    """결과값이 백만이 넘는 경우를 테스트합니다."""
    assert calculate("1000 * 2000") == 2_000_000
```

테스트를 보강한 후 다시 `uv run pytest --cov=calculator`를 실행하면, 마침내 `Cover`가 100%가 된 것을 확인할 수 있습니다.

이처럼 코드 커버리지는 단순히 숫자를 높이는 활동이 아니라, **리포트를 분석하여 테스트의 빈틈을 찾고, 코드를 더 신뢰할 수 있도록 테스트를 보강해나가는 체계적인 품질 개선 활동**입니다.

---
**다음 파트**: [Part 5. '누가' 하는가: 팀 스포츠로서의 테스트](../../05-testing-as-a-team-sport/01-tests-as-living-documentation/README.md)
