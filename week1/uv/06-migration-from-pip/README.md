# 05. 기존 pip 프로젝트를 uv로 전환하기

많은 Python 프로젝트들이 `requirements.txt` 파일을 사용하여 의존성을 관리해왔습니다. `uv`는 이러한 기존 프로젝트들을 매우 간단하게 현대적인 `pyproject.toml` 기반의 프로젝트로 전환할 수 있는 기능을 제공합니다.

이 세션에서는 `pip`와 `requirements.txt`로 관리되던 프로젝트를 `uv` 프로젝트로 마이그레이션하는 방법을 알아봅니다.

### 학습 목표

-   `requirements.txt` 기반 워크플로우의 특징을 이해합니다.
-   `uv add -r` 명령어를 사용하여 `requirements.txt` 파일의 의존성을 `pyproject.toml`로 가져올 수 있습니다.
-   개발용 의존성(`requirements-dev.txt`)을 별도의 그룹으로 마이그레이션할 수 있습니다.

---

### 1. `pip` 워크플로우 돌아보기

기존 `pip` 기반 프로젝트는 보통 다음과 같이 운영됩니다.

1.  `python -m venv .venv`로 가상 환경 생성
2.  `source .venv/bin/activate`로 가상 환경 활성화
3.  `pip install -r requirements.txt`로 의존성 설치
4.  `pip freeze > requirements.txt`로 현재 의존성 목록을 파일에 저장

이 방식은 간단하지만, 다음과 같은 단점들이 있습니다.
-   `requirements.txt`만으로는 어떤 패키지가 직접 설치한 것이고 어떤 것이 하위 의존성인지 구분하기 어렵습니다.
-   여러 플랫폼(Windows, macOS, Linux)을 동시에 지원하는 잠금 파일을 만들기가 번거롭습니다.

`uv`는 `pyproject.toml`과 `uv.lock`을 통해 이러한 문제들을 해결합니다.

---

### 2. `uv` 프로젝트로 마이그레이션하기

기존 프로젝트 폴더 안에서 몇 가지 명령어만 실행하면 마이그레이션이 완료됩니다.

#### 1단계: `uv` 프로젝트 초기화

`requirements.txt`가 있는 기존 프로젝트의 루트 디렉터리에서 `uv init`을 실행합니다.

```bash
# 기존 프로젝트 폴더로 이동했다고 가정
uv init
```

이 명령은 `pyproject.toml`과 같은 `uv` 프로젝트에 필요한 기본 파일들을 생성합니다.

#### 2단계: 의존성 가져오기

`uv add -r` 명령어는 `requirements.txt` 파일을 읽어 `pyproject.toml`로 의존성을 옮겨줍니다.

```bash
uv add -r requirements.txt
```

이 명령을 실행하면 `uv`는 다음 작업들을 자동으로 수행합니다.
1.  `requirements.txt`에 명시된 모든 패키지를 `pyproject.toml` 파일의 `[project.dependencies]` 섹션에 추가합니다.
2.  모든 의존성을 분석하여 크로스플랫폼을 지원하는 `uv.lock` 파일을 생성합니다.
3.  `.venv` 가상 환경에 실제 패키지들을 설치(동기화)합니다.

#### 3단계: 개발용 의존성 가져오기 (선택)

`pytest`, `black`처럼 개발 시에만 필요한 패키지들을 `requirements-dev.txt` 등으로 분리해서 관리했다면, `--dev` 플래그를 사용하여 가져올 수 있습니다.

```bash
uv add -r requirements-dev.txt --dev
```

이 패키지들은 `pyproject.toml` 파일의 `[tool.uv.dev-dependencies]` 라는 별도의 그룹으로 관리되어, 실제 프로덕션 의존성과 명확히 분리됩니다.

---

### 3. 마이그레이션 완료!

이제 기존의 `requirements.txt`, `requirements-dev.txt` 파일들은 더 이상 필요 없으며 삭제해도 좋습니다.

앞으로는 아래와 같이 `uv` 명령어를 사용하여 프로젝트를 관리하면 됩니다.
-   **패키지 추가**: `uv add <package_name>`
-   **패키지 설치/동기화**: `uv sync`
-   **스크립트 실행**: `uv run <script_name>`

---

### 4. `uv` 프로젝트를 `requirements.txt`로 내보내기

반대로 `uv` 프로젝트를 `pip` 환경으로 내보내야 할 경우도 있습니다. 자세한 방법은 아래 문서를 참고하세요.

-   [**uv 프로젝트에서 `requirements.txt`로 내보내기**](./exporting-to-pip.md)

---

**참고**: [uv 공식 마이그레이션 가이드](https://docs.astral.sh/uv/guides/migration/pip-to-project/)

**다음 세션**: [06. Python 버전 관리하기](../06-python-version-management/README.md)
