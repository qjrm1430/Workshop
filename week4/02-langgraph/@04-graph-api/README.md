# StateGraph API 사용법

StateGraph API는 LangGraph에서 그래프를 구성하는 고수준 API입니다. 이 섹션에서는 StateGraph를 사용하여 다양한 형태의 그래프를 만드는 방법을 알아봅니다.

## StateGraph 기본 사용법

### 1. 그래프 생성

```python
from langgraph.graph import StateGraph
from typing import TypedDict

class MyState(TypedDict):
    value: int

graph = StateGraph(MyState)
```

### 2. 노드 추가

```python
def my_node(state: MyState) -> dict:
    return {"value": state.get("value", 0) + 1}

graph.add_node("my_node", my_node)
```

### 3. 엣지 추가

```python
from langgraph.graph import START, END

graph.add_edge(START, "my_node")  # 시작 → 노드
graph.add_edge("my_node", END)    # 노드 → 종료
```

### 4. 그래프 컴파일 및 실행

```python
app = graph.compile()
result = app.invoke({"value": 0})
```

## 선형 그래프 (Linear Graph)

가장 간단한 형태의 그래프로, 노드들이 순차적으로 실행됩니다.

```python
graph = StateGraph(MyState)

graph.add_node("step1", step1_function)
graph.add_node("step2", step2_function)
graph.add_node("step3", step3_function)

graph.add_edge(START, "step1")
graph.add_edge("step1", "step2")
graph.add_edge("step2", "step3")
graph.add_edge("step3", END)

app = graph.compile()
```

## 조건부 그래프 (Conditional Graph)

상태에 따라 다른 경로로 분기하는 그래프입니다.

### 조건부 엣지 사용

```python
def route_decision(state: MyState) -> str:
    """다음 노드를 결정하는 함수"""
    value = state.get("value", 0)
    
    if value > 10:
        return "high_value_path"
    elif value > 5:
        return "medium_value_path"
    else:
        return "low_value_path"

graph.add_conditional_edges(
    "decision_node",
    route_decision,
    {
        "high_value_path": "process_high",
        "medium_value_path": "process_medium",
        "low_value_path": "process_low"
    }
)
```

## 루프가 있는 그래프

노드들이 반복적으로 실행될 수 있는 그래프입니다.

```python
def should_continue(state: MyState) -> str:
    """계속할지 종료할지 결정"""
    counter = state.get("counter", 0)
    
    if counter < 5:
        return "continue"
    else:
        return "end"

graph.add_conditional_edges(
    "loop_node",
    should_continue,
    {
        "continue": "loop_node",  # 자기 자신으로 돌아감
        "end": END
    }
)
```

## 병렬 실행

여러 노드를 동시에 실행할 수 있습니다.

```python
# 여러 노드를 동시에 실행
graph.add_edge("start", "node_a")
graph.add_edge("start", "node_b")
graph.add_edge("start", "node_c")

# 모든 노드가 완료되면 다음 노드로
graph.add_edge("node_a", "merge")
graph.add_edge("node_b", "merge")
graph.add_edge("node_c", "merge")
```

## Command를 사용한 제어 흐름

노드에서 상태 업데이트와 제어 흐름을 동시에 제어할 수 있습니다.

```python
from langgraph.types import Command
from typing import Literal

def my_node(state: MyState) -> Command[Literal["next_node", "end"]]:
    """상태 업데이트와 다음 노드를 동시에 결정"""
    value = state.get("value", 0)
    
    if value > 10:
        return Command(
            update={"value": value + 1},
            goto="next_node"
        )
    else:
        return Command(
            update={"value": value},
            goto="end"
        )

graph.add_node("my_node", my_node, ends=["next_node", "end"])
```

## 그래프 시각화

컴파일된 그래프를 시각화할 수 있습니다:

```python
app = graph.compile()

# 그래프 구조 출력
print(app.get_graph().draw_mermaid())
```

## 다음 단계

이제 StateGraph API를 사용하여 그래프를 구성하는 방법을 이해했으니, 다음 섹션에서 LangGraph의 고급 기능(체크포인팅, Human-in-the-loop, Persistence)을 알아보겠습니다.

