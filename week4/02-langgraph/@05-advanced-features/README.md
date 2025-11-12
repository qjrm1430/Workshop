# LangGraph 고급 기능

LangGraph는 프로덕션 환경에서 사용할 수 있는 강력한 고급 기능들을 제공합니다. 이 섹션에서는 Durable Execution, Human-in-the-loop, Persistence에 대해 알아봅니다.

## 1. Durable Execution (지속 가능한 실행)

Durable Execution은 에이전트가 **장애가 발생해도 지속**될 수 있게 해주는 기능입니다. 에이전트는 오랜 시간 동안 실행될 수 있으며, 중단된 지점부터 재개할 수 있습니다.

### 체크포인팅 (Checkpointing)

체크포인팅은 그래프 실행 중 상태를 주기적으로 저장하는 기능입니다. 이를 통해:
- 장애 발생 시 중단된 지점부터 재개 가능
- 장기 실행 작업의 진행 상황 추적
- 상태의 시간 여행 (Time Travel)

### 체크포인터 사용

```python
from langgraph.checkpoint.memory import MemorySaver

# 메모리 체크포인터 생성 (실험용)
checkpointer = MemorySaver()

# 그래프 컴파일 시 체크포인터 추가
app = graph.compile(checkpointer=checkpointer)

# thread_id를 사용하여 실행
config = {"configurable": {"thread_id": "thread-1"}}
result = app.invoke(initial_state, config)
```

### 프로덕션용 체크포인터

```python
# SQLite 체크포인터 (로컬 개발용)
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string(":memory:")

# Postgres 체크포인터 (프로덕션용)
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver.from_conn_string("postgresql://...")
```

## 2. Human-in-the-Loop (사람 개입)

Human-in-the-Loop는 에이전트 실행 중 **사람의 감독이나 승인**이 필요한 지점에서 실행을 일시 중지하고 입력을 받을 수 있게 해주는 기능입니다.

### Interrupt 사용

```python
from langgraph.graph import interrupt

def review_node(state: MyState):
    """검토가 필요한 노드"""
    # 실행 일시 중지 및 사용자 입력 대기
    interrupt()
    
    # 사용자 입력 후 재개
    return {"reviewed": True}
```

### Human-in-the-Loop 미들웨어 (LangChain 에이전트)

LangChain 에이전트에서는 미들웨어를 사용하여 더 쉽게 구현할 수 있습니다:

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import MemorySaver

agent = create_agent(
    model=model,
    tools=[write_file_tool, execute_sql_tool],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file": True,  # 파일 쓰기 전 승인 필요
                "execute_sql": {"allowed_decisions": ["approve", "reject"]}
            }
        )
    ],
    checkpointer=MemorySaver()
)
```

## 3. Persistence (영속성)

Persistence는 에이전트의 상태를 **영구적으로 저장**하여 세션 간에 유지할 수 있게 해주는 기능입니다.

### Thread 기반 영속성

Thread는 대화나 작업의 컨텍스트를 나타내는 개념입니다. 같은 thread_id를 사용하면 이전 상태를 불러올 수 있습니다:

```python
# 첫 번째 실행
config = {"configurable": {"thread_id": "conversation-1"}}
result1 = app.invoke({"message": "안녕하세요"}, config)

# 두 번째 실행 (이전 상태 유지)
result2 = app.invoke({"message": "이전 대화를 기억하나요?"}, config)
```

### 상태 복원

```python
# 특정 체크포인트로 복원
from langgraph.checkpoint.base import Checkpoint

# 최신 상태 가져오기
checkpoint = checkpointer.get({"configurable": {"thread_id": "thread-1"}})

# 특정 체크포인트로 복원
app.invoke(
    new_input,
    config={
        "configurable": {
            "thread_id": "thread-1",
            "checkpoint_id": checkpoint["id"]
        }
    }
)
```

## 고급 기능의 활용 사례

### 1. 장기 실행 작업

```python
# 장기 실행 작업을 체크포인팅과 함께 실행
def long_running_task(state):
    # 작업 수행
    for i in range(1000):
        # 중간에 체크포인트 저장
        if i % 100 == 0:
            # 상태 저장 (자동으로 체크포인터가 처리)
            pass
    return {"completed": True}
```

### 2. 승인이 필요한 작업

```python
def sensitive_operation(state):
    """민감한 작업 수행 전 승인 필요"""
    # 실행 일시 중지
    interrupt()
    
    # 승인 후 재개
    return {"approved": True}
```

### 3. 대화 기록 관리

```python
# 대화 세션 유지
config = {"configurable": {"thread_id": "user-123"}}

# 첫 번째 메시지
app.invoke({"messages": [{"role": "user", "content": "안녕"}]}, config)

# 두 번째 메시지 (이전 대화 기억)
app.invoke({"messages": [{"role": "user", "content": "내 이름이 뭐였지?"}]}, config)
```

## 다음 단계

이제 LangGraph의 고급 기능을 이해했으니, 다음 섹션에서 실습 프로젝트를 통해 배운 내용을 종합적으로 활용해보겠습니다.

