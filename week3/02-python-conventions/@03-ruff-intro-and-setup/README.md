# 03. Ruff 소개와 설정: Linter/Formatter를 한 번에

Ruff는 **초고속 파이썬 린터 및 포매터**입니다. 이 워크숍에서는 Ruff만 사용합니다.

## 설치 및 실행
프로젝트 루트(`week3/`)에 `pyproject.toml`이 이미 준비되어 있습니다.

```bash
uv run ruff check .
uv run ruff format .
```

## VS Code 연동
설정 예시:
```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  }
}
```

## 팀 규칙 커스터마이즈
`week3/pyproject.toml`의 `[tool.ruff]`, `[tool.ruff.lint]`, `[tool.ruff.format]`에서 규칙을 조정할 수 있습니다.
