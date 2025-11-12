# RAG (Retrieval Augmented Generation)

RAG는 **Retrieval Augmented Generation**의 약자로, LLM이 외부 지식 소스에서 정보를 검색하여 더 정확하고 맥락에 맞는 답변을 생성할 수 있게 해주는 기술입니다.

## RAG란?

RAG는 LLM의 한계를 보완하는 강력한 기법입니다. LLM은 학습 시점의 정보만 가지고 있지만, RAG를 사용하면 **실시간으로 외부 문서나 데이터베이스에서 정보를 검색**하여 최신 정보를 바탕으로 답변을 생성할 수 있습니다.

## RAG의 동작 원리

1. **문서 수집 및 인덱싱**: 관련 문서들을 수집하고 벡터 스토어에 인덱싱합니다.
2. **쿼리 처리**: 사용자의 질문을 받습니다.
3. **검색 (Retrieval)**: 사용자 질문과 관련된 문서를 벡터 스토어에서 검색합니다.
4. **증강 (Augmentation)**: 검색된 문서를 컨텍스트로 LLM에 제공합니다.
5. **생성 (Generation)**: LLM이 검색된 정보를 바탕으로 답변을 생성합니다.

## RAG의 장점

1. **최신 정보 제공**: 학습 시점 이후의 정보도 활용할 수 있습니다.
2. **정확성 향상**: 특정 도메인이나 문서에 대한 정확한 정보를 제공할 수 있습니다.
3. **출처 추적**: 어떤 문서에서 정보를 가져왔는지 추적할 수 있습니다.
4. **비용 효율성**: LLM을 재학습하지 않고도 새로운 정보를 활용할 수 있습니다.

## RAG 에이전트 vs RAG 체인

RAG를 구현하는 방법은 크게 두 가지가 있습니다:

### 1. RAG 에이전트

에이전트가 필요할 때만 검색을 수행하는 방식입니다.

**장점**:
- 필요할 때만 검색하므로 효율적입니다.
- 인사말이나 간단한 질문에는 검색을 하지 않습니다.
- 여러 번의 검색을 수행할 수 있습니다.

**단점**:
- 검색이 필요할 때 두 번의 LLM 호출이 필요합니다 (검색 쿼리 생성 + 최종 응답).
- LLM이 검색을 건너뛸 수 있습니다.

### 2. RAG 체인

항상 검색을 수행하고 결과를 컨텍스트로 제공하는 방식입니다.

**장점**:
- 쿼리당 한 번의 LLM 호출만 필요하므로 빠릅니다.
- 항상 검색을 수행하므로 일관성이 있습니다.

**단점**:
- 불필요한 검색을 수행할 수 있습니다.
- 유연성이 떨어집니다.

## RAG 에이전트 구현 예제

```python
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 문서 로드 및 분할
loader = TextLoader("document.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(documents)

# 2. 벡터 스토어 생성
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)

# 3. 검색 도구 생성
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """문서에서 관련 정보를 검색합니다."""
    retrieved_docs = vectorstore.similarity_search(query, k=2)
    serialized = "\n\n".join(
        f"Source: {doc.metadata}\nContent: {doc.page_content}"
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

# 4. 에이전트 생성
model = ChatOpenAI(model="gpt-3.5-turbo")
agent = create_agent(
    model=model,
    tools=[retrieve_context],
    system_prompt="문서에서 정보를 검색하여 사용자의 질문에 답변하세요."
)
```

## RAG 체인 구현 예제

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# 벡터 스토어에서 검색
retrieved_docs = vectorstore.similarity_search(user_query, k=2)
context = "\n\n".join(doc.page_content for doc in retrieved_docs)

# 프롬프트에 컨텍스트 포함
prompt = ChatPromptTemplate.from_messages([
    ("system", "다음 문서를 참고하여 질문에 답변하세요:\n\n{context}"),
    ("user", "{question}")
])

# 체인 구성 및 실행
chain = prompt | model
response = chain.invoke({"context": context, "question": user_query})
```

## RAG의 활용 사례

1. **고객 지원 챗봇**: 회사 문서나 FAQ를 검색하여 정확한 답변 제공
2. **법률 문서 분석**: 법률 문서에서 관련 조항 검색 및 해석
3. **의료 진단 지원**: 의학 문헌에서 증상 관련 정보 검색
4. **기술 문서 Q&A**: 기술 문서에서 관련 정보 검색 및 설명

## 다음 단계

이제 RAG의 기본 개념을 이해했으니, 다음 섹션에서 실습 프로젝트를 통해 배운 내용을 종합적으로 활용해보겠습니다.

