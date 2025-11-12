"""
조건부 그래프 예제

이 예제는 상태에 따라 다른 경로로 분기하는 조건부 그래프를 보여줍니다.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class DecisionState(TypedDict):
    value: int
    path: str
    result: str


def input_node(state: DecisionState) -> dict:
    """입력 노드: 초기 값 설정"""
    value = state.get("value", 0)
    return {"result": f"입력 값: {value}"}


def route_decision(state: DecisionState) -> str:
    """라우팅 결정 함수"""
    value = state.get("value", 0)
    
    if value > 10:
        return "high"
    elif value > 5:
        return "medium"
    else:
        return "low"


def process_high(state: DecisionState) -> dict:
    """높은 값 처리"""
    value = state.get("value", 0)
    result = state.get("result", "")
    return {
        "path": "high",
        "result": f"{result}\n[높은 값 처리] {value}는 큰 값입니다. 특별 처리를 수행합니다."
    }


def process_medium(state: DecisionState) -> dict:
    """중간 값 처리"""
    value = state.get("value", 0)
    result = state.get("result", "")
    return {
        "path": "medium",
        "result": f"{result}\n[중간 값 처리] {value}는 중간 값입니다. 일반 처리를 수행합니다."
    }


def process_low(state: DecisionState) -> dict:
    """낮은 값 처리"""
    value = state.get("value", 0)
    result = state.get("result", "")
    return {
        "path": "low",
        "result": f"{result}\n[낮은 값 처리] {value}는 작은 값입니다. 기본 처리를 수행합니다."
    }


def main():
    # 그래프 생성
    graph = StateGraph(DecisionState)
    
    # 노드 추가
    graph.add_node("input", input_node)
    graph.add_node("high", process_high)
    graph.add_node("medium", process_medium)
    graph.add_node("low", process_low)
    
    # 엣지 추가
    graph.add_edge(START, "input")
    
    # 조건부 엣지 추가
    graph.add_conditional_edges(
        "input",
        route_decision,
        {
            "high": "high",
            "medium": "medium",
            "low": "low"
        }
    )
    
    # 모든 경로가 종료로 수렴
    graph.add_edge("high", END)
    graph.add_edge("medium", END)
    graph.add_edge("low", END)
    
    # 그래프 컴파일
    app = graph.compile()
    
    # 테스트 케이스
    test_cases = [
        {"value": 15, "path": "", "result": ""},  # 높은 값
        {"value": 7, "path": "", "result": ""},   # 중간 값
        {"value": 3, "path": "", "result": ""},   # 낮은 값
    ]
    
    print("=== 조건부 그래프 예제 ===\n")
    
    for i, initial_state in enumerate(test_cases, 1):
        print(f"테스트 케이스 {i}: value = {initial_state['value']}")
        result = app.invoke(initial_state)
        print(f"선택된 경로: {result['path']}")
        print(f"결과:\n{result['result']}\n")


if __name__ == "__main__":
    main()

