"""
체크포인팅 예제

이 예제는 LangGraph의 체크포인팅 기능을 보여줍니다.
장애 발생 시 중단된 지점부터 재개할 수 있습니다.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


class TaskState(TypedDict):
    step: int
    progress: str
    completed: bool


def step1(state: TaskState) -> dict:
    """1단계 작업"""
    return {
        "step": 1,
        "progress": "1단계 완료",
        "completed": False
    }


def step2(state: TaskState) -> dict:
    """2단계 작업"""
    return {
        "step": 2,
        "progress": "2단계 완료",
        "completed": False
    }


def step3(state: TaskState) -> dict:
    """3단계 작업"""
    return {
        "step": 3,
        "progress": "3단계 완료",
        "completed": True
    }


def main():
    # 그래프 생성
    graph = StateGraph(TaskState)
    
    # 노드 추가
    graph.add_node("step1", step1)
    graph.add_node("step2", step2)
    graph.add_node("step3", step3)
    
    # 엣지 추가
    graph.add_edge(START, "step1")
    graph.add_edge("step1", "step2")
    graph.add_edge("step2", "step3")
    graph.add_edge("step3", END)
    
    # 체크포인터 생성
    checkpointer = MemorySaver()
    
    # 그래프 컴파일 (체크포인터 포함)
    app = graph.compile(checkpointer=checkpointer)
    
    # thread_id 설정
    config = {"configurable": {"thread_id": "task-1"}}
    
    print("=== 체크포인팅 예제 ===\n")
    
    # 초기 상태
    initial_state = {
        "step": 0,
        "progress": "시작",
        "completed": False
    }
    
    # 실행 (각 단계마다 체크포인트가 저장됨)
    print("작업 실행 중...")
    result = app.invoke(initial_state, config)
    
    print(f"최종 상태: {result}")
    
    # 체크포인트 확인
    print("\n=== 체크포인트 확인 ===")
    checkpoint = checkpointer.get(config)
    if checkpoint:
        print(f"체크포인트 ID: {checkpoint['id']}")
        print(f"저장된 상태: {checkpoint['channel_values']}")


if __name__ == "__main__":
    main()

