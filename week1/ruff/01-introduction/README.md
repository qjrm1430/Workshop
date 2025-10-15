# 01. Ruff: 차세대 Python 린터와 포맷터

이 워크샵의 두 번째 주인공, `Ruff`에 대해 알아봅니다. `Ruff`는 `uv`를 개발한 Astral 사에서 만든 **차세대 Python 린터**(Linter)이자 **코드 포맷터**(Formatter)입니다.

Rust로 작성되어 기존의 어떤 도구보다도 **10배에서 100배 이상 빠른 속도**를 자랑하며, `Flake8`, `isort`, `Black` 등 수많은 개별 도구들의 기능을 하나로 통합하여 개발 환경을 혁신적으로 단순화시켜 줍니다.

### 학습 목표

-   `Ruff`가 무엇이며 왜 필요한지 이해합니다.
-   `Ruff`의 압도적인 속도와 **올인원**(All-in-One) 기능의 장점을 설명할 수 있습니다.
-   `uv`를 사용하여 `Ruff`를 설치하고 기본적인 검사 및 자동 수정을 수행할 수 있습니다.

---

### 1. 왜 Ruff를 사용해야 할까요?

#### 압도적인 속도

`Ruff`를 사용하는 가장 큰 이유는 속도입니다. 기존 린터들이 수십 초에서 몇 분씩 걸리던 작업을 `Ruff`는 1초 미만으로 완료합니다. 이는 개발자가 코드를 작성하고 저장할 때마다 실시간에 가까운 피드백을 받을 수 있게 해줍니다.

아래는 CPython 코드베이스 전체를 린팅하는 데 걸리는 시간을 비교한 벤치마크입니다.

![Ruff Linter Performance Benchmark](https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg#only-dark)
*출처: Ruff 공식*

#### 올인원(All-in-One) 도구

이전에는 각기 다른 역할을 하는 여러 도구를 조합해서 사용해야 했습니다.

-   **코드 스타일 검사**: `Flake8`, `Pylint`
-   **import 정렬**: `isort`
-   **코드 포맷팅**: `Black`
-   **불필요한 코드 제거**: `autoflake`
-   **docstring 스타일 검사**: `pydocstyle`

`Ruff`는 이 모든 도구의 핵심 기능을 `ruff`라는 단일 명령어로 통합하여 제공합니다. 더 이상 복잡한 설정을 하거나 여러 도구의 버전을 맞추느라 고생할 필요가 없습니다.

#### `uv`와의 완벽한 시너지

`Ruff`는 `uv`와 같은 개발사에서 만들어져 서로 완벽하게 통합됩니다. `uv`를 통해 `Ruff`를 설치하고 실행하는 과정은 매우 간단하며, `pyproject.toml`을 중심으로 한 현대적인 Python 프로젝트 관리 방식의 핵심적인 부분을 담당합니다.

---

### 2. `uv`와 함께 Ruff 시작하기 (미니 튜토리얼)

`uv` 프로젝트에서 `Ruff`를 얼마나 쉽게 사용할 수 있는지 직접 체험해 보겠습니다.

#### 1단계: `uv` 프로젝트 생성 및 파일 작성

먼저 `uv`로 새 프로젝트를 만들고, `Ruff`가 지적할 만한 간단한 코드를 작성합니다.

```bash
# numbers 라는 이름의 uv 프로젝트 생성
uv init numbers
cd numbers

# main.py 파일 생성
# os 모듈을 import했지만 사용하지 않았습니다.
echo "import os

def my_sum(a, b):
  return a+b" > main.py
```

#### 2단계: `Ruff` 설치

`uv`를 사용해 `Ruff`를 개발용 의존성으로 추가합니다.

```bash
uv add --dev ruff
```

#### 3단계: 코드 검사하기

`uv run`을 사용해 `Ruff`로 코드를 검사합니다.

```bash
uv run ruff check .
```

`Ruff`는 즉시 `main.py` 파일의 문제를 찾아내고, 사용하지 않는 `import os` 구문이 있다는 것을 알려줄 것입니다.

```
main.py:1:8: F401 [*] `os` imported but unused
  |
1 | import os
  |        ^^ F401
2 |
3 | def my_sum(a, b):
  |
  = [*] 1 fixable error detected.
```

#### 4단계: 자동으로 문제 수정하기

`Ruff`의 가장 강력한 기능 중 하나는 자동 수정입니다. `--fix` 플래그를 추가하여 다시 실행해 보세요.

```bash
uv run ruff check . --fix
```

이제 `main.py` 파일을 다시 열어보면, 불필요했던 `import os` 라인이 자동으로 삭제된 것을 확인할 수 있습니다.

---

**참고 문서**
- [Ruff 공식 홈페이지](https://docs.astral.sh/ruff/)

**다음 세션**: [02. Ruff 설치 및 에디터 연동](./../02-installation-setup/README.md)
