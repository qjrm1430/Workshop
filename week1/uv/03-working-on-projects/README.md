# 03. uv 프로젝트 시작하기

이전 세션에서 `uv` 설치를 마쳤으니, 이제 `uv`를 사용하여 실제 Python 프로젝트를 만들고 관리하는 방법을 알아보겠습니다.

`uv`는 `pyproject.toml` 파일을 중심으로 프로젝트의 정보와 의존성을 체계적으로 관리합니다.

### 학습 목표

-   `uv init` 명령어로 새로운 Python 프로젝트를 생성할 수 있습니다.
-   `pyproject.toml`, `.venv`, `uv.lock` 등 `uv` 프로젝트의 핵심 구조를 이해합니다.
-   `uv add`, `uv remove` 명령어로 프로젝트 의존성을 관리할 수 있습니다.
-   `uv run` 명령어로 프로젝트 환경에서 스크립트를 실행할 수 있습니다.

---

### 1. 새 프로젝트 생성하기

`uv init` 명령어를 사용하면 새로운 Python 프로젝트를 간편하게 시작할 수 있습니다.

```bash
# 'my-project' 라는 이름의 새 프로젝트 폴더를 만들고 이동합니다.
uv init my-project
cd my-project
```

명령이 실행되면, `uv`는 다음과 같은 기본 프로젝트 구조를 생성합니다.

```
.
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

`main.py`에는 간단한 "Hello world" 코드가 들어있습니다. `uv run` 명령어로 바로 실행해볼 수 있습니다.

```bash
uv run main.py
```

```
# 출력 결과
Hello from my-project!
```

---

### 2. 프로젝트 핵심 구조 이해하기

`uv` 프로젝트는 몇 가지 중요한 파일과 디렉터리로 구성됩니다. `uv run`이나 `uv add` 같은 명령어를 처음 실행하면, `uv`가 알아서 `.venv` 가상 환경과 `uv.lock` 파일을 생성해줍니다.

#### `pyproject.toml`

프로젝트의 모든 설정이 담긴 가장 중요한 파일입니다. 프로젝트 이름, 버전, 설명 같은 메타데이터와 의존성 패키지 목록이 이 파일에 기록됩니다.

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
dependencies = [] # 여기에 의존성 패키지가 추가됩니다.
```

#### `.venv`

프로젝트를 위한 독립된 Python 환경(가상 환경)입니다. 프로젝트 의존성은 모두 이곳에 설치되어 다른 프로젝트나 시스템 파이썬과 섞이지 않습니다.

#### `uv.lock`

프로젝트 의존성의 "족보"와 같은 잠금 파일입니다. `pyproject.toml`에는 `requests`처럼 간단히 기록하지만, `uv.lock`에는 실제 설치된 `requests`의 정확한 버전(예: `2.31.0`)과 그 하위 의존성들의 모든 정보가 기록됩니다. 이 파일을 Git에 함께 커밋하면, 동료 개발자나 배포 서버 등 어디서든 **항상 동일한 버전의 패키지를 설치**할 수 있어 예측 가능한 환경을 보장합니다.

---

### 3. 의존성 관리하기

`pip`처럼 패키지를 설치하고 삭제하는 명령어입니다. 차이점은 `uv add`를 실행하면 `pyproject.toml`과 `uv.lock` 파일이 자동으로 업데이트된다는 것입니다.

#### 패키지 추가

```bash
# requests 패키지를 프로젝트에 추가합니다.
uv add requests

# 특정 버전을 지정하여 추가할 수도 있습니다.
uv add "requests==2.31.0"

# Git 저장소에 있는 패키지를 직접 추가할 수도 있습니다.
uv add git+https://github.com/psf/requests
```

#### 패키지 삭제

```bash
uv remove requests
```

#### 의존성 트리 확인 (uv tree)

`uv tree` 명령어를 사용하면 현재 프로젝트에 설치된 패키지들의 의존성 관계를 나무 구조로 한눈에 파악할 수 있습니다. 어떤 패키지가 다른 패키지를 필요로 하는지 추적하거나, 복잡한 의존성 문제를 디버깅할 때 매우 유용합니다.

예를 들어, `flask` 패키지를 추가한 후 `uv tree`를 실행하면 다음과 같은 결과를 볼 수 있습니다.

```bash
# flask가 설치된 상태라고 가정
uv tree
```

```
# 출력 예시
myproject v0.1.0
└── flask v3.1.2
    ├── blinker v1.9.0
    ├── click v8.3.0
    │   └── colorama v0.4.6
    ├── itsdangerous v2.2.0
    ├── jinja2 v3.1.6
    │   └── markupsafe v3.0.3
    ├── markupsafe v3.0.3
    └── werkzeug v3.1.3
        └── markupsafe v3.0.3
```

위 결과를 통해 `flask`가 `blinker`, `click`, `Jinja2` 등 여러 패키지에 의존하고 있으며, `Jinja2`는 또다시 `MarkupSafe`에 의존하고 있음을 명확히 알 수 있습니다.

---

### 4. 프로젝트 환경에서 명령어 실행하기

`uv run`은 프로젝트의 가상 환경(`.venv`) 안에서 명령어나 스크립트를 실행해주는 매우 편리한 기능입니다.

`uv run`을 사용하면 `uv`가 자동으로 **"현재 환경이 최신 상태인가?"** 를 점검하고, 필요하다면 `uv.lock`을 기준으로 패키지를 설치/업데이트한 후 명령을 실행합니다. 덕분에 우리는 수동으로 가상 환경을 활성화하거나 `pip install`을 신경 쓸 필요가 없습니다.

#### Flask 웹 서버 실행 예시

```bash
# 1. flask 패키지를 추가합니다.
uv add flask

# 2. uv run 으로 flask 개발 서버를 실행합니다.
# (명령어와 인자는 -- 뒤에 공백을 두고 입력합니다.)
uv run -- flask run -p 3000
```

#### 직접 가상 환경 활성화하기 (참고)

물론 기존 방식처럼 가상 환경을 직접 활성화해서 사용할 수도 있습니다.

-   **macOS / Linux**
    ```bash
    uv sync  # 먼저 환경을 최신 상태로 동기화
    source .venv/bin/activate
    flask run -p 3000
    ```
-   **Windows**
    ```powershell
    uv sync  # 먼저 환경을 최신 상태로 동기화
    .venv\Scripts\activate
    flask run -p 3000
    ```

---

**참고**: [uv 공식 프로젝트 가이드](https://docs.astral.sh/uv/guides/projects/)

**다음 세션**: [04. 도구 사용하기](../04-tools/README.md)
