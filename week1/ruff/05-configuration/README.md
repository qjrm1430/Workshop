# 05. Ruff 설정 종합 (`pyproject.toml`)

`Ruff`의 모든 설정은 `uv`와 마찬가지로 `pyproject.toml` 파일을 통해 중앙에서 관리됩니다. 이를 통해 프로젝트의 모든 팀원이 동일한 코드 스타일과 린팅 규칙을 공유할 수 있습니다.

이전 세션들에서 Linter와 Formatter의 개념을 배웠으니, 이제 `pyproject.toml` 안의 `[tool.ruff]` 테이블을 통해 이 두 도구의 동작을 프로젝트 요구사항에 맞게 통합 설정하는 방법을 알아봅니다.

### 학습 목표

-   `pyproject.toml` 파일에 `[tool.ruff]` 테이블을 추가하여 Linter와 Formatter를 함께 설정할 수 있습니다.
-   `select`, `ignore` 옵션을 사용하여 Linter가 검사할 규칙을 관리할 수 있습니다.
-   `line-length` 등 Formatter의 주요 옵션을 설정할 수 있습니다.
-   특정 파일이나 디렉터리에만 다른 규칙을 적용하는 방법을 이해합니다.

---

### 1. `[tool.ruff]` 테이블 구조

모든 `Ruff` 설정은 `pyproject.toml` 파일의 `[tool.ruff]` 테이블 아래에 작성합니다. 이 테이블은 크게 Linter 설정을 위한 `[tool.ruff.lint]`와 Formatter 설정을 위한 `[tool.ruff.format]`으로 나뉩니다.

기본적인 구조는 다음과 같습니다.

```toml
# pyproject.toml

[tool.ruff]
# 여기에 linter와 formatter에 공통으로 적용될 옵션을 작성합니다.
line-length = 88 # 한 줄의 최대 길이를 88자로 제한 (Black과 동일)
target-version = "py39" # 대상 파이썬 버전을 3.9로 지정

# 검사에서 제외할 파일/디렉터리 목록
exclude = [".venv", "docs"]

# Linter 관련 설정
[tool.ruff.lint]
# 여기에 linter 규칙 등을 설정합니다.

# Formatter 관련 설정
[tool.ruff.format]
# 여기에 코드 포맷팅 스타일 등을 설정합니다.
```

---

### 2. Linter와 Formatter 설정 예제

아래는 일반적인 Python 프로젝트에서 사용할 수 있는 `pyproject.toml`의 `[tool.ruff]` 설정 예제입니다. 각 옵션의 역할은 주석을 통해 확인할 수 있습니다.

-   [**`pyproject.toml` 설정 예제 파일**](./examples/pyproject.toml)

이 파일을 직접 살펴보며 각 옵션이 Linter와 Formatter에 어떻게 영향을 미치는지 확인해 보세요.

#### 주요 설정 다시보기

-   **`select`**: 활성화할 Linter 규칙 코드를 지정합니다. `["E", "F", "B", "I"]` 처럼 여러 규칙 그룹을 선택할 수 있습니다.
-   **`ignore`**: `select`로 선택된 규칙 중 특정 규칙을 비활성화합니다.
-   **`per-file-ignores`**: `tests/*` 처럼 특정 파일 패턴에 대해서만 특정 규칙을 무시할 때 사용합니다.
-   **`line-length`**: Formatter가 코드를 정리할 때 기준으로 삼는 최대 라인 길이입니다.
-   **`quote-style`**: Formatter가 사용할 따옴표 스타일(`"double"` 또는 `'single'`)을 지정합니다.

---

**참고 문서**
- [Ruff 공식 설정 가이드](https://docs.astral.sh/ruff/configuration/)

**워크샵을 마치며**

이것으로 `uv`와 `Ruff`를 사용한 현대적인 Python 개발 환경 구성 워크샵을 마칩니다. 여러분은 이제 Python 프로젝트의 의존성을 빠르고 안정적으로 관리하고, 일관되고 품질 높은 코드를 손쉽게 작성할 수 있는 강력한 도구를 갖추게 되었습니다.
