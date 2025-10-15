# 02. uv 설치 및 설정

이 세션에서는 각자의 운영체제(OS)에 `uv`를 설치하고, 개발 환경을 설정하는 방법을 알아봅니다.

### 학습 목표

-   자신의 운영체제에 맞는 방법으로 `uv`를 설치할 수 있습니다.
-   설치가 잘 되었는지 명령어를 통해 확인할 수 있습니다.
-   (선택) 더 편리한 사용을 위해 셸 자동 완성을 설정할 수 있습니다.

---

### 1. Standalone 설치 (권장)

가장 간단하고 공식적으로 권장되는 설치 방법입니다. 운영체제에 맞는 아래 명령어를 터미널에 입력해주세요.

#### macOS 및 Linux

`curl`을 사용한 설치:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows

`PowerShell`을 사용한 설치:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **-ExecutionPolicy ByPass 란?**
> Windows의 보안 정책상 인터넷에서 받은 스크립트는 바로 실행할 수 없습니다. 이 옵션은 이번 한 번만 정책을 우회하여 설치 스크립트를 실행하도록 허용하는 역할을 합니다.

---

### 2. 설치 확인

설치가 완료되었다면, 터미널을 새로 열고 아래 명령어를 입력하여 `uv`의 버전이 정상적으로 출력되는지 확인합니다.

```bash
uv --version
```

```
# 출력 예시
uv 0.2.14
```

---

### 3. (선택) 다른 설치 방법

이미 다른 패키지 매니저에 익숙하다면, 아래 방법들을 사용할 수도 있습니다.

-   **Homebrew (macOS)**
    ```bash
    brew install uv
    ```
-   **WinGet (Windows)**
    ```bash
    winget install --id=astral-sh.uv -e
    ```
-   **pipx (모든 OS)**
    - `pipx`는 파이썬 CLI 도구를 시스템에 독립적으로 설치해주는 유용한 도구입니다.
    ```bash
    pipx install uv
    ```

---

### 4. uv 업그레이드

Standalone 방식으로 설치한 경우, 아래 명령어로 `uv`를 최신 버전으로 업데이트할 수 있습니다.

```bash
uv self update
```

---

**참고**: [uv 공식 설치 문서](https://docs.astral.sh/uv/getting-started/installation/)

**다음 세션**: [03. 기본 명령어 알아보기](../03-basic-commands/README.md)
