# 02. Ruff 설치 및 에디터 연동

`Ruff`를 효과적으로 사용하기 위해서는 프로젝트에 설치하고, 매일 사용하는 코드 에디터와 연동하여 실시간 피드백을 받는 환경을 구축하는 것이 중요합니다.

이 세션에서는 `uv`를 사용하여 `Ruff`를 설치하는 가장 권장되는 방법을 알아보고, VS Code에서 `Ruff` 확장 프로그램을 설정하는 방법을 안내합니다.

### 학습 목표

-   `uv`를 사용하여 프로젝트에 `Ruff`를 설치할 수 있습니다.
-   VS Code에 `Ruff` 확장 프로그램을 설치하고 기본 설정을 완료할 수 있습니다.
-   파일 저장 시 자동으로 포맷팅 및 수정 기능이 동작하도록 설정할 수 있습니다.

---

### 1. `uv`로 Ruff 설치하기 (권장)

이 워크샵에서는 `uv`를 사용하여 `Ruff`를 **프로젝트의 개발용 의존성(`dev dependency`)으로 설치**하는 방법을 사용합니다. 이 방식은 프로젝트 팀원 모두가 동일한 버전의 `Ruff`를 사용하도록 보장해주기 때문에 협업 시 가장 권장되는 방법입니다.

프로젝트 루트 디렉터리에서 아래 명령어를 실행하세요.

```bash
uv add --dev ruff
```

이 명령어는 `ruff`를 `pyproject.toml`의 `[tool.uv.dev-dependencies]` 그룹에 추가하고, `.venv` 가상 환경에 설치합니다.

이제 `uv run`을 통해 `Ruff`의 기능을 사용할 수 있습니다.

```bash
# 버전 확인
uv run ruff --version

# 현재 디렉터리 코드 검사 (린팅)
uv run ruff check .

# 현재 디렉터리 코드 포맷팅
uv run ruff format .
```

#### 참고: 다른 설치 방법들

`uv`를 사용하지 않는 환경을 위해 다른 설치 방법들도 간단히 소개합니다.

-   **pip 사용**: `pip install ruff`
-   **pipx 사용 (전역 설치)**: `pipx install ruff`
-   **Homebrew (macOS)**: `brew install ruff`
-   **Conda**: `conda install -c conda-forge ruff`

---

### 2. VS Code 확장 프로그램 설치 및 설정

`Ruff`의 진정한 강력함은 코드 에디터와 연동될 때 나타납니다. 코드를 작성하고 저장하는 순간마다 실시간으로 문제를 찾아주고, 자동으로 코드를 정리해주기 때문입니다.

#### 1단계: 확장 프로그램 설치

1.  VS Code를 엽니다.
2.  왼쪽의 확장 프로그램(Extensions) 탭을 엽니다. (단축키: `Ctrl+Shift+X`)
3.  검색창에 `Ruff`를 검색합니다.
4.  `Astral`에서 게시한 공식 `Ruff` 확장 프로그램을 찾아 `Install` 버튼을 클릭합니다.

#### 2단계: VS Code 설정 (`settings.json`)

`Ruff` 확장 프로그램이 파일을 저장할 때마다 자동으로 코드 검사 및 포맷팅을 수행하도록 설정하는 것이 매우 편리합니다.

1.  `Ctrl+Shift+P`를 눌러 커맨드 팔레트를 엽니다.
2.  `Preferences: Open User Settings (JSON)`을 검색하여 선택합니다.
3.  열리는 `settings.json` 파일에 아래 내용을 추가합니다.

```json
{
    // "[python]": { ... } 블록 안에 아래 내용들을 추가합니다.
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff", // Python 포맷터를 Ruff로 지정
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",    // 저장 시 가능한 모든 문제를 자동으로 수정
            "source.organizeImports": "explicit" // 저장 시 import 구문을 자동으로 정리
        }
    },

    // Ruff 관련 추가 설정 (선택 사항)
    "ruff.lint.args": [
        "--select=ALL" // 기본 규칙 외에 모든 규칙을 활성화 (프로젝트에 맞게 조정 필요)
    ]
}
```

이제 Python 파일을 저장(`Ctrl+S`)할 때마다, `Ruff`가 자동으로 불필요한 코드를 수정하고, `import` 순서를 정리하며, 코드 스타일을 일관되게 맞춰줄 것입니다.

---

**참고 문서**
- [Ruff 공식 설치 가이드](https://docs.astral.sh/ruff/installation/)
- [Ruff VS Code 확장 프로그램](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

**다음 세션**: [03. Ruff 설정하기 (`pyproject.toml`)](./../03-configuration/README.md)
