# 05. `pyproject.toml` 이해하고 설정하기

`uv` 프로젝트의 중심에는 `pyproject.toml` 파일이 있습니다. 이 파일은 Python 표준(PEP 621)에 따라 프로젝트의 정보, 의존성, 그리고 빌드 설정을 정의하는 중앙 허브 역할을 합니다.

이 세션에서는 `uv` 프로젝트에서 `pyproject.toml`을 어떻게 구성하고 활용하는지, 자주 사용되는 설정들을 중심으로 알아봅니다.

### 학습 목표

-   `pyproject.toml`의 역할과 기본 구조를 이해합니다.
-   `[project]` 테이블을 사용하여 프로젝트의 기본 정보와 의존성을 정의할 수 있습니다.
-   의존성 그룹(development, custom)을 만들어 프로젝트를 체계적으로 관리할 수 있습니다.
-   `[tool.uv.sources]`를 사용하여 로컬(local) 또는 Git 저장소의 패키지를 의존성으로 추가할 수 있습니다.
-   워크스페이스(Workspaces)를 사용하여 여러 패키지를 모노레포(monorepo) 방식으로 관리할 수 있습니다.

---

### 1. `pyproject.toml`의 기본 구조

`pyproject.toml` 파일은 여러 "테이블(table)"로 구성됩니다. `uv` 프로젝트에서는 주로 `[project]`와 `[tool.uv]` 테이블을 사용하게 됩니다.

#### `[project]` 테이블: 표준 프로젝트 정보

이 테이블에는 프로젝트의 이름, 버전, 의존성 등 PEP 621 표준에 명시된 핵심 정보가 들어갑니다.

-   `name`: 프로젝트의 고유한 이름입니다. (필수)
-   `version`: 프로젝트의 현재 버전입니다. (필수)
-   `description`: 프로젝트에 대한 한 줄 설명입니다.
-   `requires-python`: 프로젝트가 호환되는 Python 버전 명세입니다. (예: `">=3.9"`)
-   `dependencies`: 프로젝트의 핵심 의존성 패키지 목록입니다. `uv add`로 추가한 패키지들이 여기에 기록됩니다.

#### `[tool.uv]` 테이블: `uv` 전용 설정 및 의존성 그룹

이 테이블은 `uv`의 고유한 설정이나 표준 `[project]` 테이블에서 지원하지 않는 추가 기능을 정의하는 데 사용됩니다. 가장 대표적인 것이 **의존성 그룹**(dependency groups)과 **소스**(sources)입니다.

-   **개발용 의존성**: `[tool.uv.dev-dependencies]` 테이블을 사용하여 `pytest`, `ruff`처럼 개발 시에만 필요한 패키지를 분리할 수 있습니다. `uv add --dev <package>`로 추가하면 여기에 기록됩니다.

-   **사용자 정의 그룹**: `[tool.uv.dependencies.{group-name}]` 형태로 `docs`(문서), `test`(테스트) 등 원하는 목적에 따라 그룹을 자유롭게 만들 수 있습니다. `uv add --group <group-name> <package>`로 추가합니다.

---

### 2. 고급 의존성 관리: `[tool.uv.sources]`

프로젝트를 하다 보면 PyPI에 등록된 패키지 외에, 로컬 폴더에 있는 다른 프로젝트나 Git 저장소에 있는 패키지를 의존성으로 사용해야 할 때가 있습니다. 이때 `[tool.uv.sources]` 테이블을 사용합니다.

```toml
[project]
dependencies = [
    "my-local-library",
    "some-library-from-git",
]

[tool.uv.sources]
# 로컬 경로 의존성: `path` 키를 사용합니다.
my-local-library = { path = "../my-local-library" }

# Git 의존성: `git` 키를 사용합니다.
some-library-from-git = { git = "https://github.com/user/repo.git" }
```
`uv`는 이렇게 지정된 의존성을 PyPI가 아닌 해당 소스에서 가져와 설치합니다.

---

### 3. 워크스페이스(Workspaces): 모노레포 관리

하나의 Git 저장소 안에서 여러 개의 Python 패키지(예: 웹 서버, 공용 라이브러리, 관리자 도구)를 함께 개발하는 것을 **모노레포**(Monorepo)라고 합니다.

`uv`의 워크스페이스는 이런 모노레포를 효율적으로 관리하기 위한 기능입니다. 워크스페이스를 사용하면 여러 패키지가 각자의 `pyproject.toml`을 가지면서도, **하나의 `uv.lock` 파일과 하나의 가상 환경(`.venv`)을 공유**하게 됩니다. 이를 통해 모든 패키지가 동일한 버전의 의존성을 사용하도록 보장할 수 있습니다.

워크스페이스 설정은 루트 `pyproject.toml` 파일에 `[tool.uv.workspace]` 테이블을 추가하여 정의합니다.

---

### 4. `pyproject.toml` 예제 살펴보기

말로만 설명하는 것보다 실제 예제를 보는 것이 가장 좋습니다. 아래에 네 가지 대표적인 시나리오에 대한 `pyproject.toml` 예제 파일을 준비했습니다.

각 파일의 주석을 꼼꼼히 읽어보며 각 설정이 어떤 의미를 가지는지 파악해보세요.

-   [**예제 1: 기본적인 프로젝트**](./examples/01-basic-project.toml)
    -   가장 단순한 형태의 `pyproject.toml` 구조를 보여줍니다.
-   [**예제 2: 개발용 의존성 분리**](./examples/02-dev-dependencies.toml)
    -   `[tool.uv.dev-dependencies]`를 사용해 프로덕션 의존성과 개발용 의존성을 분리하는 방법을 보여줍니다.
-   [**예제 3: 사용자 정의 그룹 사용**](./examples/03-custom-groups.toml)
    -   `docs`, `test` 등 커스텀 그룹을 만들어 의존성을 더 체계적으로 관리하는 방법을 보여줍니다.
-   [**예제 4: 워크스페이스 (모노레포)**](./examples/04-workspace-example/pyproject.toml)
    -   여러 하위 패키지를 하나의 워크스페이스로 묶어 관리하는 방법을 보여줍니다.

---

**참고 문서**
- [uv 공식 문서 - 의존성 관리](https://docs.astral.sh/uv/concepts/projects/dependencies/)
- [uv 공식 문서 - 워크스페이스 사용하기](https://docs.astral.sh/uv/concepts/projects/workspaces/)

**다음 세션**: [06. pip 프로젝트를 uv로 마이그레이션하기](../06-migration-from-pip/README.md)
