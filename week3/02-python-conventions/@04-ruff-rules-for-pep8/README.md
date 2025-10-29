# 04. Ruff 규칙으로 PEP 8 지키기

Ruff는 PEP8 관련 규칙들을 묶어 제공합니다.

## 주요 선택 규칙
- `F`, `E`, `W`: Pyflakes/pycodestyle 범주
- `I`: import 정렬(isort)
- `B`: bugbear (잠재적 버그 감지)

예시 설정(`pyproject.toml`):
```toml
[tool.ruff.lint]
select = ["F", "E", "W", "I", "B"]
ignore = ["E501"]
```

## 실습
```bash
uv run ruff check week3/02-python-conventions --fix
uv run ruff format week3/02-python-conventions
```

보고서의 출력에서 규칙 코드를 확인하고, 필요시 ignore/target-version/line-length 등을 조정합니다.
