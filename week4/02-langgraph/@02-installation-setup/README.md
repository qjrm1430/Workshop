# LangGraph 설치 및 환경 설정

## 사전 요구사항

- Python 3.10 이상
- `uv` 패키지 관리자 (이 워크샵에서는 `uv`를 사용합니다)

## 설치 방법

### 1. 기본 LangGraph 패키지 설치

LangGraph의 핵심 패키지를 설치합니다:

```bash
uv add langgraph
```

### 2. LangChain 설치 (선택사항)

LangGraph는 독립적으로 사용할 수 있지만, 모델과 도구를 통합하기 위해 LangChain을 함께 사용하는 것이 일반적입니다:

```bash
uv add langchain
```

### 3. 모델 제공자 패키지 설치

사용하려는 LLM 제공자에 맞는 패키지를 설치합니다:

```bash
# OpenAI 사용 시
uv add langchain-openai

# Anthropic 사용 시
uv add langchain-anthropic
```

### 4. 체크포인터 패키지 설치 (선택사항)

영속성 기능을 사용하려면 체크포인터 패키지를 설치해야 합니다:

```bash
# SQLite 체크포인터 (실험 및 로컬 워크플로우용)
uv add langgraph-checkpoint-sqlite

# Postgres 체크포인터 (프로덕션용)
uv add langgraph-checkpoint-postgres
```

## 환경 변수 설정

LLM 제공자의 API 키를 환경 변수로 설정해야 합니다. 자세한 내용은 LangChain 설치 섹션을 참조하세요.

## 간단한 테스트

설치가 제대로 되었는지 확인하기 위해 간단한 테스트를 해봅시다:

```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# 상태 정의
class State(TypedDict):
    message: str

# 노드 정의
def my_node(state: State) -> State:
    return {"message": f"Hello, {state.get('message', 'World')}!"}

# 그래프 생성
graph = StateGraph(State)
graph.add_node("my_node", my_node)
graph.add_edge(START, "my_node")
graph.add_edge("my_node", END)

# 그래프 컴파일 및 실행
app = graph.compile()
result = app.invoke({"message": "LangGraph"})
print(result["message"])  # "Hello, LangGraph!"
```

## week4 워크샵 환경 설정

이 워크샵에서는 `week4/pyproject.toml`에 필요한 모든 패키지가 정의되어 있습니다. 다음 명령어로 한 번에 설치할 수 있습니다:

```bash
cd week4
uv sync --dev
```

이 명령어는 다음 패키지들을 설치합니다:
- `langgraph`: LangGraph 핵심 패키지
- `langchain`: LangChain (모델 및 도구 통합용)
- `langchain-openai`: OpenAI 통합
- `langchain-anthropic`: Anthropic 통합
- `langchain-community`: 커뮤니티 통합

## 다음 단계

설치가 완료되었으니, 다음 섹션에서 LangGraph의 핵심 개념(State, Nodes, Edges)을 자세히 알아보겠습니다.

