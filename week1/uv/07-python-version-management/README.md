# 07. `uv`로 Python 버전 관리하기

`uv`는 패키지 관리뿐만 아니라, `conda`처럼 **Python 자체를 설치하고 관리하는 강력한 기능**을 내장하고 있습니다. 이를 통해 개발자는 시스템에 설치된 Python 버전에 구애받지 않고, 프로젝트마다 필요한 특정 버전의 Python을 독립적으로 사용할 수 있습니다.

이 세션에서는 `uv`를 사용하여 Python을 설치하고, 프로젝트별로 버전을 고정(pin)하는 방법을 알아봅니다.

### 학습 목표

-   `uv`의 "관리되는(managed)" Python과 "시스템(system)" Python의 차이를 이해합니다.
-   `uv python install` 명령어로 원하는 버전의 Python을 설치할 수 있습니다.
-   `uv python list`로 설치 가능한 Python 버전 목록을 확인할 수 있습니다.
-   `.python-version` 파일과 `uv python pin`을 사용하여 프로젝트의 Python 버전을 명시적으로 고정할 수 있습니다.

---

### 1. `uv`의 Python 버전 관리 개념

`uv`는 두 종류의 Python 설치를 구분하여 인식합니다.

-   **시스템(System) Python**: 운영체제에 기본적으로 설치되어 있거나, `conda`, `Homebrew` 등을 통해 사용자가 직접 설치한 모든 Python을 의미합니다.
-   **관리되는(Managed) Python**: `uv python install` 명령어를 통해 `uv`가 직접 다운로드하고 설치한 Python을 의미합니다. 이 Python들은 `uv`의 관리 디렉터리(예: `~/.local/share/uv/python`)에 격리되어 설치됩니다.

`uv`는 기본적으로 **관리되는 Python을 우선적으로 사용**하지만, 만약 없다면 시스템 Python을 찾아 사용합니다.

---

### 2. Python 설치 및 확인

#### Python 설치하기: `uv python install`

`conda install python=3.11`과 유사하게, `uv python install` 명령어로 원하는 버전의 Python을 쉽게 설치할 수 있습니다.

```bash
# 특정 버전(3.11.6) 설치
uv python install 3.11.6

# 특정 마이너 버전의 최신 패치 버전(예: 3.12.4) 설치
uv python install 3.12

# 여러 버전 동시에 설치
uv python install 3.9 3.10
```

#### 설치 가능한 버전 목록 보기: `uv python list`

설치할 수 있는 CPython, PyPy 등의 전체 버전 목록을 확인할 수 있습니다.

```bash
uv python list
```

---

### 3. 프로젝트별 Python 버전 고정하기

`uv`는 `.python-version`이라는 파일을 통해 해당 프로젝트가 어떤 Python 버전을 사용해야 하는지 명시하는 방식을 지원합니다.

#### 버전 고정하기: `uv python pin`

프로젝트 루트 디렉터리에서 `uv python pin`을 실행하면 `.python-version` 파일이 생성되고, `uv`는 앞으로 이 프로젝트에서 해당 버전을 기본으로 사용합니다.

```bash
# 현재 프로젝트에서 사용할 Python 버전을 3.11로 지정
uv python pin 3.11
```

이 명령을 실행하면 현재 디렉터리에 `.python-version` 파일이 생성되고, 그 안에는 `3.11`이라는 내용이 기록됩니다.

이제부터 이 프로젝트 폴더 안에서 `uv add`, `uv run`, `uv sync` 등의 `uv` 명령을 실행하면, `uv`는 자동으로 Python 3.11을 찾아 가상 환경을 구성하고 명령을 실행합니다. 만약 3.11 버전이 `uv`에 의해 관리되고 있지 않다면, `uv`는 자동으로 해당 버전을 다운로드하여 설치합니다.

이 `.python-version` 파일을 Git에 함께 커밋하면, 팀 동료 누구나 `uv`를 통해 동일한 Python 버전으로 개발 환경을 구성할 수 있게 됩니다.

---

**참고 문서**
- [uv 공식 문서 - Python 버전 관리](https://docs.astral.sh/uv/concepts/python-versions/)

**다음 세션**: [Ruff 시작하기](../ruff/01-introduction/README.md)
