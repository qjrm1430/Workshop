"""
상태 관리 예제

이 예제는 LangGraph에서 상태를 관리하는 방법을 보여줍니다.
여러 노드가 상태를 읽고 업데이트하는 방법을 학습합니다.
"""

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END


# State 정의: 대화 메시지와 메타데이터를 포함
class ConversationState(TypedDict):
    messages: List[str]  # 대화 메시지 목록
    user_name: str       # 사용자 이름
    message_count: int   # 메시지 개수


# 노드 1: 사용자 인사
def greet_user(state: ConversationState) -> dict:
    """사용자를 인사하는 노드"""
    user_name = state.get("user_name", "Guest")
    messages = state.get("messages", [])
    
    greeting = f"안녕하세요, {user_name}님!"
    new_messages = messages + [greeting]
    
    return {
        "messages": new_messages,
        "message_count": len(new_messages)
    }


# 노드 2: 메시지 처리
def process_message(state: ConversationState) -> dict:
    """메시지를 처리하는 노드"""
    messages = state.get("messages", [])
    user_name = state.get("user_name", "Guest")
    
    # 마지막 메시지에 응답
    if messages:
        last_message = messages[-1]
        response = f"{user_name}님의 메시지를 처리했습니다: {last_message}"
    else:
        response = "처리할 메시지가 없습니다."
    
    new_messages = messages + [response]
    
    return {
        "messages": new_messages,
        "message_count": len(new_messages)
    }


# 노드 3: 요약 생성
def summarize_conversation(state: ConversationState) -> dict:
    """대화를 요약하는 노드"""
    messages = state.get("messages", [])
    message_count = state.get("message_count", 0)
    
    summary = f"총 {message_count}개의 메시지가 교환되었습니다."
    new_messages = messages + [f"[요약] {summary}"]
    
    return {
        "messages": new_messages,
        "message_count": len(new_messages)
    }


def main():
    # 그래프 생성
    graph = StateGraph(ConversationState)
    
    # 노드 추가
    graph.add_node("greet", greet_user)
    graph.add_node("process", process_message)
    graph.add_node("summarize", summarize_conversation)
    
    # 엣지 추가
    graph.add_edge(START, "greet")
    graph.add_edge("greet", "process")
    graph.add_edge("process", "summarize")
    graph.add_edge("summarize", END)
    
    # 그래프 컴파일
    app = graph.compile()
    
    # 초기 상태 설정
    initial_state = {
        "messages": [],
        "user_name": "홍길동",
        "message_count": 0
    }
    
    # 그래프 실행
    print("=== 상태 관리 예제 ===\n")
    print(f"초기 상태: {initial_state}\n")
    
    result = app.invoke(initial_state)
    
    print("=== 실행 결과 ===")
    print(f"사용자 이름: {result['user_name']}")
    print(f"메시지 개수: {result['message_count']}")
    print("\n메시지 목록:")
    for i, msg in enumerate(result['messages'], 1):
        print(f"  {i}. {msg}")


if __name__ == "__main__":
    main()

