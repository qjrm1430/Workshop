"""
선형 그래프 예제

이 예제는 노드들이 순차적으로 실행되는 선형 그래프를 보여줍니다.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class ProcessingState(TypedDict):
    data: str
    step: int
    result: str


def step1_validate(state: ProcessingState) -> dict:
    """1단계: 데이터 검증"""
    data = state.get("data", "")
    return {
        "step": 1,
        "result": f"[검증] 데이터: {data}"
    }


def step2_process(state: ProcessingState) -> dict:
    """2단계: 데이터 처리"""
    data = state.get("data", "")
    result = state.get("result", "")
    processed = data.upper()
    return {
        "step": 2,
        "result": f"{result}\n[처리] 변환된 데이터: {processed}"
    }


def step3_save(state: ProcessingState) -> dict:
    """3단계: 결과 저장"""
    result = state.get("result", "")
    return {
        "step": 3,
        "result": f"{result}\n[저장] 결과가 저장되었습니다."
    }


def main():
    # 그래프 생성
    graph = StateGraph(ProcessingState)
    
    # 노드 추가
    graph.add_node("validate", step1_validate)
    graph.add_node("process", step2_process)
    graph.add_node("save", step3_save)
    
    # 선형 엣지 추가
    graph.add_edge(START, "validate")
    graph.add_edge("validate", "process")
    graph.add_edge("process", "save")
    graph.add_edge("save", END)
    
    # 그래프 컴파일
    app = graph.compile()
    
    # 실행
    print("=== 선형 그래프 예제 ===\n")
    
    initial_state = {
        "data": "hello world",
        "step": 0,
        "result": ""
    }
    
    result = app.invoke(initial_state)
    
    print("실행 결과:")
    print(result["result"])
    print(f"\n최종 단계: {result['step']}")


if __name__ == "__main__":
    main()

