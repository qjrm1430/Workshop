"""
간단한 LangGraph 예제

이 예제는 LangGraph의 기본 개념(State, Nodes, Edges)을 보여줍니다.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. State 정의
class MyState(TypedDict):
    message: str
    counter: int


# 2. Nodes 정의
def start_node(state: MyState) -> dict:
    """시작 노드: 메시지를 초기화합니다."""
    return {"message": "Hello", "counter": 0}


def process_node(state: MyState) -> dict:
    """처리 노드: 메시지를 처리하고 카운터를 증가시킵니다."""
    current_message = state.get("message", "")
    current_counter = state.get("counter", 0)
    
    new_message = f"{current_message}, LangGraph!"
    new_counter = current_counter + 1
    
    return {"message": new_message, "counter": new_counter}


def end_node(state: MyState) -> dict:
    """종료 노드: 최종 메시지를 출력합니다."""
    message = state.get("message", "")
    counter = state.get("counter", 0)
    
    final_message = f"{message} (처리 횟수: {counter})"
    return {"message": final_message}


def main():
    # 3. 그래프 생성
    graph = StateGraph(MyState)
    
    # 4. 노드 추가
    graph.add_node("start", start_node)
    graph.add_node("process", process_node)
    graph.add_node("end", end_node)
    
    # 5. 엣지 추가
    graph.add_edge(START, "start")
    graph.add_edge("start", "process")
    graph.add_edge("process", "end")
    graph.add_edge("end", END)
    
    # 6. 그래프 컴파일
    app = graph.compile()
    
    # 7. 그래프 실행
    print("=== 간단한 그래프 실행 ===\n")
    
    initial_state = {"message": "", "counter": 0}
    result = app.invoke(initial_state)
    
    print(f"최종 메시지: {result['message']}")
    print(f"최종 카운터: {result['counter']}")


if __name__ == "__main__":
    main()

