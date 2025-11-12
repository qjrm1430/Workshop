"""
도구 사용 예제

이 예제는 에이전트가 여러 도구를 조합하여 사용하는 방법을 보여줍니다.
"""

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from datetime import datetime


# 도구 1: 현재 시간 조회
@tool
def get_current_time() -> str:
    """현재 시간을 반환합니다."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 도구 2: 계산기
@tool
def calculate(expression: str) -> str:
    """수학 표현식을 계산합니다.
    
    Args:
        expression: 계산할 수학 표현식 (예: "2 + 3 * 4")
        
    Returns:
        계산 결과
    """
    try:
        result = eval(expression)  # 실제 프로덕션에서는 eval 사용 금지!
        return f"계산 결과: {result}"
    except Exception as e:
        return f"계산 오류: {str(e)}"


# 도구 3: 문자열 변환
@tool
def convert_string(text: str, operation: str) -> str:
    """문자열에 다양한 변환을 적용합니다.
    
    Args:
        text: 변환할 문자열
        operation: 변환 종류 ('upper', 'lower', 'reverse', 'length')
        
    Returns:
        변환된 결과
    """
    operations = {
        "upper": text.upper(),
        "lower": text.lower(),
        "reverse": text[::-1],
        "length": f"문자열 길이: {len(text)}"
    }
    return operations.get(operation, f"알 수 없는 연산: {operation}")


def main():
    # 모델 초기화
    model = ChatOpenAI(model="gpt-3.5-turbo")

    # 에이전트 생성
    agent = create_agent(
        model=model,
        tools=[get_current_time, calculate, convert_string],
        system_prompt=(
            "당신은 다양한 도구를 사용하여 사용자의 요청을 처리하는 유용한 어시스턴트입니다. "
            "사용자의 요청에 가장 적합한 도구를 선택하여 사용하세요."
        )
    )

    # 예제 1: 시간 조회
    print("=== 예제 1: 현재 시간 조회 ===\n")
    response1 = agent.invoke({
        "messages": [{"role": "user", "content": "지금 몇 시인가요?"}]
    })
    print(f"응답: {response1['messages'][-1].content}\n")

    # 예제 2: 계산
    print("=== 예제 2: 수학 계산 ===\n")
    response2 = agent.invoke({
        "messages": [{"role": "user", "content": "25 * 4 + 10을 계산해주세요."}]
    })
    print(f"응답: {response2['messages'][-1].content}\n")

    # 예제 3: 문자열 변환
    print("=== 예제 3: 문자열 변환 ===\n")
    response3 = agent.invoke({
        "messages": [{"role": "user", "content": "'Hello World'를 대문자로 변환하고 길이를 알려주세요."}]
    })
    print(f"응답: {response3['messages'][-1].content}\n")


if __name__ == "__main__":
    main()

