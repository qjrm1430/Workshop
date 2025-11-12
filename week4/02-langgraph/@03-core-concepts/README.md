# LangGraph 핵심 개념

LangGraph는 에이전트 워크플로우를 **그래프**로 모델링합니다. 그래프는 세 가지 핵심 구성 요소로 이루어져 있습니다: **State**, **Nodes**, **Edges**.

## 1. State (상태)

State는 애플리케이션의 **현재 스냅샷**을 나타내는 공유 데이터 구조입니다. 모든 노드가 이 상태를 읽고 쓸 수 있으며, 그래프 실행 중 상태가 진화합니다.

### State 정의

State는 일반적으로 TypedDict를 사용하여 정의합니다:

```python
from typing import TypedDict

class MyState(TypedDict):
    messages: list  # 대화 메시지
    counter: int    # 카운터
    data: dict      # 기타 데이터
```

### State 업데이트

노드는 상태를 읽고 업데이트할 수 있습니다. 노드는 상태의 일부만 업데이트할 수 있으며, LangGraph가 자동으로 병합합니다:

```python
def my_node(state: MyState) -> dict:
    # 현재 상태 읽기
    current_counter = state.get("counter", 0)
    
    # 상태 업데이트 (일부만 반환)
    return {"counter": current_counter + 1}
```

## 2. Nodes (노드)

Nodes는 에이전트의 **로직을 인코딩하는 함수**입니다. 현재 상태를 입력으로 받아, 일부 계산이나 부작용을 수행하고, 업데이트된 상태를 반환합니다.

### 노드의 특징

- **함수**: 노드는 단순히 Python 함수입니다 (동기 또는 비동기)
- **입력**: 현재 상태와 설정(config)을 받습니다
- **출력**: 상태 업데이트를 반환합니다
- **유연성**: LLM을 포함할 수도 있고, 일반 코드만 포함할 수도 있습니다

### 노드 정의 예제

```python
def process_message(state: MyState) -> dict:
    """메시지를 처리하는 노드"""
    messages = state.get("messages", [])
    last_message = messages[-1] if messages else None
    
    # 메시지 처리 로직
    processed = f"Processed: {last_message}"
    
    return {"messages": messages + [processed]}

def call_llm(state: MyState) -> dict:
    """LLM을 호출하는 노드"""
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="gpt-3.5-turbo")
    messages = state.get("messages", [])
    
    response = model.invoke(messages)
    
    return {"messages": messages + [response]}
```

## 3. Edges (엣지)

Edges는 현재 상태를 기반으로 **다음에 실행할 노드를 결정**하는 함수입니다. 조건부 분기나 고정 전환을 정의할 수 있습니다.

### 엣지의 종류

1. **고정 엣지 (Fixed Edges)**: 항상 같은 노드로 이동
2. **조건부 엣지 (Conditional Edges)**: 상태에 따라 다른 노드로 이동

### 고정 엣지 예제

```python
from langgraph.graph import START, END

graph = StateGraph(MyState)
graph.add_edge(START, "first_node")      # 시작 → 첫 번째 노드
graph.add_edge("first_node", "second_node")  # 첫 번째 → 두 번째 노드
graph.add_edge("second_node", END)       # 두 번째 노드 → 종료
```

### 조건부 엣지 예제

```python
def should_continue(state: MyState) -> str:
    """다음 노드를 결정하는 조건부 엣지"""
    messages = state.get("messages", [])
    last_message = messages[-1] if messages else None
    
    if last_message and hasattr(last_message, "tool_calls"):
        return "call_tools"  # 도구 호출이 필요하면
    else:
        return "end"  # 그렇지 않으면 종료

graph.add_conditional_edges(
    "agent",
    should_continue,
    {
        "call_tools": "tools",
        "end": END
    }
)
```

## 그래프 실행 흐름

LangGraph는 Google의 Pregel 알고리즘에서 영감을 받아 **이산적인 "super-step"**으로 실행됩니다:

1. **초기화**: 모든 노드가 비활성 상태로 시작
2. **활성화**: 노드는 들어오는 엣지에서 새 메시지(상태)를 받으면 활성화
3. **실행**: 활성 노드가 함수를 실행하고 업데이트를 반환
4. **전파**: 업데이트가 다음 노드로 전파
5. **종료**: 모든 노드가 비활성이고 전송 중인 메시지가 없으면 종료

## 핵심 개념 요약

- **State**: 공유 데이터 구조, 모든 노드가 읽고 쓸 수 있음
- **Nodes**: 로직을 수행하는 함수, 상태를 입력받아 업데이트를 반환
- **Edges**: 다음 노드를 결정하는 함수, 고정 또는 조건부

**핵심 원칙**: "노드는 작업을 수행하고, 엣지는 다음에 무엇을 할지 알려줍니다."

## 다음 단계

이제 핵심 개념을 이해했으니, 다음 섹션에서 StateGraph API를 사용하여 실제 그래프를 구성하는 방법을 알아보겠습니다.

