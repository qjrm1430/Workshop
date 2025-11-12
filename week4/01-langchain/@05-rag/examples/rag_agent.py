"""
RAG 에이전트 예제

이 예제는 RAG 에이전트를 구현하는 방법을 보여줍니다.
에이전트가 필요할 때만 검색을 수행합니다.
"""

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


# 문서 데이터 준비
sample_documents = [
    "LangChain은 LLM을 활용하여 에이전트와 애플리케이션을 구축하기 위한 프레임워크입니다.",
    "LangGraph는 상태 기반 에이전트 오케스트레이션 프레임워크입니다.",
    "RAG는 Retrieval Augmented Generation의 약자로, 외부 지식 소스에서 정보를 검색하여 답변을 생성합니다.",
    "에이전트는 LLM이 도구를 사용하여 복잡한 작업을 수행할 수 있게 해주는 시스템입니다.",
]

# 벡터 스토어 생성 (전역 변수로 관리)
embeddings = OpenAIEmbeddings()
documents = [Document(page_content=doc) for doc in sample_documents]
vectorstore = FAISS.from_documents(documents, embeddings)


# 검색 도구 정의
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """문서에서 관련 정보를 검색합니다.
    
    Args:
        query: 검색할 질문이나 키워드
        
    Returns:
        검색된 문서 내용과 원본 문서 객체
    """
    retrieved_docs = vectorstore.similarity_search(query, k=2)
    serialized = "\n\n".join(
        f"Source: {doc.metadata}\nContent: {doc.page_content}"
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


def main():
    print("=== RAG 에이전트 예제 ===\n")
    
    # 모델 초기화
    model = ChatOpenAI(model="gpt-3.5-turbo")
    
    # 에이전트 생성
    agent = create_agent(
        model=model,
        tools=[retrieve_context],
        system_prompt=(
            "당신은 문서 기반 질의응답 시스템입니다. "
            "사용자의 질문에 답하기 위해 필요할 때 문서를 검색하세요. "
            "간단한 인사말이나 일반적인 질문에는 검색 없이 답변할 수 있습니다."
        )
    )
    
    # 질문 테스트
    questions = [
        "안녕하세요!",
        "LangChain이란 무엇인가요?",
        "RAG는 무엇의 약자인가요?",
    ]
    
    for question in questions:
        print(f"질문: {question}")
        response = agent.invoke({
            "messages": [{"role": "user", "content": question}]
        })
        print(f"답변: {response['messages'][-1].content}\n")
        
        # 도구 호출 내역 확인
        for msg in response["messages"]:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                print("  [검색 도구 사용됨]")
                break


if __name__ == "__main__":
    main()

