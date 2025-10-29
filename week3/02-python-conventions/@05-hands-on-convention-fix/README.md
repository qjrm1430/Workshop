# 05. 핸즈온: Ruff로 컨벤션 바로잡기

## 준비
- `@03-ruff-intro-and-setup/examples/`에 예제 파일을 준비합니다.

## 실습 단계
1. 린트 실행: `uv run ruff check .`
2. 자동 수정: `uv run ruff check . --fix` + `uv run ruff format .`
3. 남은 경고 분석: 필요시 `pyproject.toml`에서 규칙 조정
4. import 정렬과 네이밍 확인

## 완료 기준
- 경고가 의미있게 줄어들었고, 포맷이 일관적이다.
- 팀 합의된 규칙(라인 길이 등)이 반영되었다.
