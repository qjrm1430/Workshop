"""
RAG 체인 예제

이 예제는 RAG 체인을 구현하는 방법을 보여줍니다.
항상 검색을 수행하고 결과를 컨텍스트로 제공합니다.
"""

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_rag_chain():
    """RAG 체인을 생성합니다."""
    
    # 1. 문서 로드 (실제로는 파일에서 로드하지만, 여기서는 예제 데이터 사용)
    sample_documents = [
        "LangChain은 LLM을 활용하여 에이전트와 애플리케이션을 구축하기 위한 프레임워크입니다.",
        "LangGraph는 상태 기반 에이전트 오케스트레이션 프레임워크입니다.",
        "RAG는 Retrieval Augmented Generation의 약자로, 외부 지식 소스에서 정보를 검색하여 답변을 생성합니다.",
        "에이전트는 LLM이 도구를 사용하여 복잡한 작업을 수행할 수 있게 해주는 시스템입니다.",
    ]
    
    # 2. 문서를 Document 객체로 변환
    from langchain_core.documents import Document
    documents = [Document(page_content=doc) for doc in sample_documents]
    
    # 3. 문서 분할
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    splits = text_splitter.split_documents(documents)
    
    # 4. 벡터 스토어 생성
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splits, embeddings)
    
    # 5. 모델 초기화
    model = ChatOpenAI(model="gpt-3.5-turbo")
    
    # 6. 프롬프트 템플릿 생성
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "당신은 문서 기반 질의응답 시스템입니다. "
            "다음 문서를 참고하여 사용자의 질문에 정확하게 답변하세요.\n\n"
            "참고 문서:\n{context}"
        )),
        ("user", "{question}")
    ])
    
    # 7. RAG 체인 함수 정의
    def rag_chain(question: str):
        # 검색 수행
        retrieved_docs = vectorstore.similarity_search(question, k=2)
        context = "\n\n".join(doc.page_content for doc in retrieved_docs)
        
        # 체인 실행
        chain = prompt | model
        response = chain.invoke({"context": context, "question": question})
        return response.content
    
    return rag_chain


def main():
    print("=== RAG 체인 예제 ===\n")
    
    # RAG 체인 생성
    rag = create_rag_chain()
    
    # 질문 테스트
    questions = [
        "LangChain이란 무엇인가요?",
        "RAG는 무엇의 약자인가요?",
        "에이전트는 무엇을 하는 시스템인가요?",
    ]
    
    for question in questions:
        print(f"질문: {question}")
        answer = rag(question)
        print(f"답변: {answer}\n")


if __name__ == "__main__":
    main()

