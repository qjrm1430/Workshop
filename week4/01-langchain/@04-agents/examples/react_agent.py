"""
ReAct 패턴을 사용한 에이전트 예제

이 예제는 ReAct 패턴을 따르는 에이전트를 만드는 방법을 보여줍니다.
에이전트는 추론(Reasoning)과 행동(Acting)을 번갈아가며 수행합니다.
"""

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool


# 도구 1: 날씨 조회
@tool
def get_weather(city: str) -> str:
    """특정 도시의 현재 날씨 정보를 조회합니다.
    
    Args:
        city: 날씨를 조회할 도시 이름
        
    Returns:
        해당 도시의 날씨 정보
    """
    # 실제로는 날씨 API를 호출하지만, 여기서는 시뮬레이션
    weather_data = {
        "서울": "15도, 맑음",
        "부산": "18도, 구름 조금",
        "제주": "20도, 맑음"
    }
    return weather_data.get(city, f"{city}의 날씨 정보를 찾을 수 없습니다.")


# 도구 2: 옷차림 추천
@tool
def recommend_clothing(temperature: int, condition: str) -> str:
    """온도와 날씨 조건에 맞는 옷차림을 추천합니다.
    
    Args:
        temperature: 온도 (섭씨)
        condition: 날씨 조건 (예: 맑음, 비, 눈)
        
    Returns:
        추천 옷차림
    """
    if temperature < 10:
        return "따뜻한 코트, 목도리, 장갑을 추천합니다."
    elif temperature < 20:
        return "가벼운 재킷이나 가디건을 추천합니다."
    else:
        return "가벼운 옷차림이 적합합니다."


def main():
    # 모델 초기화
    model = ChatOpenAI(model="gpt-3.5-turbo")

    # 에이전트 생성
    agent = create_agent(
        model=model,
        tools=[get_weather, recommend_clothing],
        system_prompt=(
            "당신은 날씨 정보를 제공하고 옷차림을 추천하는 도우미입니다. "
            "사용자의 요청에 따라 먼저 날씨 정보를 조회하고, "
            "그 정보를 바탕으로 적절한 옷차림을 추천해주세요."
        )
    )

    # 에이전트 실행
    print("=== ReAct 에이전트 예제 ===\n")
    
    user_query = "서울의 날씨를 알려주고, 그 온도에 맞는 옷차림을 추천해주세요."
    print(f"사용자: {user_query}\n")
    
    response = agent.invoke({
        "messages": [{"role": "user", "content": user_query}]
    })

    # 최종 응답 출력
    print("에이전트 응답:")
    print(response["messages"][-1].content)
    
    # 에이전트가 사용한 도구 호출 내역 확인
    print("\n=== 도구 호출 내역 ===")
    for msg in response["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for tool_call in msg.tool_calls:
                print(f"- 도구: {tool_call['name']}")
                print(f"  인자: {tool_call['args']}")


if __name__ == "__main__":
    main()

