"""
Human-in-the-Loop 예제

이 예제는 LangGraph의 Human-in-the-Loop 기능을 보여줍니다.
실행 중 사용자 입력을 받을 수 있습니다.

참고: 실제로는 interrupt()를 사용하지만, 
이 예제는 개념을 설명하기 위해 시뮬레이션합니다.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


class ReviewState(TypedDict):
    action: str
    approved: bool
    feedback: str
    result: str


def propose_action(state: ReviewState) -> dict:
    """작업 제안"""
    action = state.get("action", "파일 삭제")
    return {
        "action": action,
        "result": f"제안된 작업: {action}"
    }


def wait_for_approval(state: ReviewState) -> dict:
    """승인 대기 (시뮬레이션)"""
    # 실제로는 interrupt()를 사용하여 실행을 일시 중지
    # 여기서는 시뮬레이션을 위해 승인 상태를 직접 설정
    action = state.get("action", "")
    
    # 사용자 승인 시뮬레이션
    approved = True  # 실제로는 사용자 입력을 받음
    feedback = "승인됨" if approved else "거부됨"
    
    return {
        "approved": approved,
        "feedback": feedback,
        "result": f"{state.get('result', '')}\n[승인 상태] {feedback}"
    }


def execute_action(state: ReviewState) -> dict:
    """작업 실행"""
    if state.get("approved", False):
        action = state.get("action", "")
        return {
            "result": f"{state.get('result', '')}\n[실행] {action} 작업이 완료되었습니다."
        }
    else:
        return {
            "result": f"{state.get('result', '')}\n[취소] 작업이 취소되었습니다."
        }


def main():
    # 그래프 생성
    graph = StateGraph(ReviewState)
    
    # 노드 추가
    graph.add_node("propose", propose_action)
    graph.add_node("approval", wait_for_approval)
    graph.add_node("execute", execute_action)
    
    # 엣지 추가
    graph.add_edge(START, "propose")
    graph.add_edge("propose", "approval")
    graph.add_edge("approval", "execute")
    graph.add_edge("execute", END)
    
    # 체크포인터 생성 (Human-in-the-Loop에 필요)
    checkpointer = MemorySaver()
    
    # 그래프 컴파일
    app = graph.compile(checkpointer=checkpointer)
    
    # 실행
    print("=== Human-in-the-Loop 예제 ===\n")
    
    initial_state = {
        "action": "중요한 파일 삭제",
        "approved": False,
        "feedback": "",
        "result": ""
    }
    
    config = {"configurable": {"thread_id": "review-1"}}
    
    result = app.invoke(initial_state, config)
    
    print("실행 결과:")
    print(result["result"])
    print(f"\n승인 상태: {result['approved']}")
    print(f"피드백: {result['feedback']}")


if __name__ == "__main__":
    main()

