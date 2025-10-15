# `uv` 프로젝트에서 `requirements.txt`로 내보내기

`uv` 프로젝트는 `pyproject.toml`과 `uv.lock`을 중심으로 의존성을 관리하지만, 때로는 `pip`만 지원하는 오래된 배포 환경이나 `uv`를 사용하지 않는 동료와 협업하기 위해 `requirements.txt` 파일이 필요할 수 있습니다.

`uv`는 `uv export` 명령어를 통해 `uv.lock` 파일에 기록된 의존성을 `requirements.txt` 포맷으로 손쉽게 내보내는 기능을 제공합니다.

---

### 1. 기본 의존성 내보내기

프로젝트의 핵심 의존성을 `requirements.txt` 파일로 추출하는 가장 기본적인 방법입니다.

프로젝트 루트 디렉터리에서 아래 명령어를 실행하세요.

```bash
uv export -o requirements.txt
```

이 명령은 `uv.lock` 파일을 읽어 의존성을 분석한 후, 모든 패키지의 버전이 고정된 `requirements.txt` 파일을 생성합니다. `uv.lock` 파일 자체가 크로스플랫폼을 지원하므로, 이렇게 생성된 `requirements.txt` **역시 기본적으로 모든 운영체제에서 호환**됩니다.

---

### 2. 해시(Hash) 없이 내보내기

`pip`의 `--require-hashes` 옵션을 사용하지 않는 환경에서는 각 라인 끝에 붙는 `--hash=...` 부분이 불필요하거나 문제를 일으킬 수 있습니다.

`--no-hashes` 플래그를 추가하면 해시 정보 없이 깔끔한 `requirements.txt` 파일을 생성할 수 있습니다.

```bash
uv export -o requirements.txt --no-hashes
```

---

### 3. 개발용 의존성 함께 내보내기

`--dev` 옵션으로 추가했던 개발용 의존성을 포함하여 `requirements-dev.txt` 파일을 만들고 싶을 때는 `--all-groups` 옵션을 사용합니다.

```bash
uv export --all-groups -o requirements-dev.txt --no-hashes
```

`--all-groups`는 `[tool.uv.dev-dependencies]`를 포함한 모든 추가 의존성 그룹과 기본 의존성을 함께 내보냅니다.

만약 **오직 개발용 의존성 그룹만** 별도로 내보내고 싶다면 `--only-group` 옵션을 사용할 수 있습니다.

```bash
uv export --only-group dev -o requirements-dev-only.txt --no-hashes
```

---
**참고**: [uv CLI 레퍼런스 - uv export](https://docs.astral.sh/uv/reference/cli/#uv-export)
