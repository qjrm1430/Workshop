"""
간단한 LangChain 체인 예제

이 예제는 LangChain의 기본적인 체인 사용법을 보여줍니다.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 모델 초기화
model = ChatOpenAI(model="gpt-3.5-turbo")

# 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다. 사용자의 질문에 명확하고 도움이 되는 답변을 제공하세요."),
    ("user", "{input}")
])

# 체인 구성: 프롬프트 → 모델
chain = prompt | model

# 체인 실행
if __name__ == "__main__":
    response = chain.invoke({"input": "파이썬에서 리스트를 정렬하는 방법을 알려주세요."})
    print("응답:", response.content)

