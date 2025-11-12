"""
기본 LangChain 에이전트 예제

이 예제는 create_agent를 사용하여 간단한 에이전트를 만드는 방법을 보여줍니다.
"""

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool


# 도구 정의: 계산기
@tool
def calculate(expression: str) -> str:
    """수학 표현식을 계산합니다. 예: '2 + 3 * 4'"""
    try:
        result = eval(expression)  # 실제 프로덕션에서는 eval 사용 금지!
        return f"계산 결과: {result}"
    except Exception as e:
        return f"계산 오류: {str(e)}"


# 도구 정의: 문자열 길이 계산
@tool
def get_string_length(text: str) -> str:
    """문자열의 길이를 반환합니다."""
    return f"문자열 '{text}'의 길이는 {len(text)}입니다."


def main():
    # 모델 초기화
    model = ChatOpenAI(model="gpt-3.5-turbo")

    # 에이전트 생성
    agent = create_agent(
        model=model,
        tools=[calculate, get_string_length],
        system_prompt="당신은 수학 계산과 문자열 처리를 도와주는 유용한 어시스턴트입니다."
    )

    # 에이전트 실행
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": "2 + 3 * 4를 계산해주세요."}
        ]
    })

    # 최종 응답 출력
    print("에이전트 응답:")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()

