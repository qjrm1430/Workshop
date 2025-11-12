# LangChain 핵심 개념

LangChain을 효과적으로 사용하기 위해 이해해야 할 핵심 개념들을 살펴보겠습니다.

## 1. 모델 (Models)

모델은 에이전트의 **추론 엔진**입니다. 에이전트의 의사결정 프로세스를 주도하며, 어떤 도구를 호출할지, 결과를 어떻게 해석할지, 언제 최종 답변을 제공할지 결정합니다.

### 모델의 주요 기능

- **텍스트 생성**: 인간처럼 텍스트를 해석하고 생성
- **도구 호출 (Tool Calling)**: 외부 도구(데이터베이스 쿼리, API 호출 등)를 호출하고 결과를 응답에 활용
- **구조화된 출력 (Structured Output)**: 정의된 형식을 따르도록 모델의 응답을 제한
- **멀티모달리티 (Multimodality)**: 텍스트 외에 이미지, 오디오, 비디오 등 처리 및 반환
- **추론 (Reasoning)**: 결론에 도달하기 위한 다단계 추론 수행

### 모델 사용 예제

```python
from langchain_openai import ChatOpenAI

# 모델 초기화
model = ChatOpenAI(model="gpt-3.5-turbo")

# 간단한 호출
response = model.invoke("파이썬에서 리스트를 정렬하는 방법을 알려주세요.")
print(response.content)
```

## 2. 도구 (Tools)

도구는 에이전트가 외부 세계와 상호작용할 수 있게 해주는 함수입니다. 데이터베이스 쿼리, API 호출, 파일 읽기/쓰기 등 다양한 작업을 수행할 수 있습니다.

### 도구 생성

LangChain에서는 `@tool` 데코레이터를 사용하여 도구를 쉽게 만들 수 있습니다:

```python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """특정 도시의 날씨를 조회합니다."""
    # 실제로는 날씨 API를 호출
    return f"{city}의 날씨는 맑음입니다."

@tool
def calculate(expression: str) -> float:
    """수학 표현식을 계산합니다."""
    return eval(expression)  # 실제 프로덕션에서는 eval 사용 금지!
```

### 도구 실행 루프

모델이 도구 호출을 반환하면, 도구를 실행하고 결과를 다시 모델에 전달해야 합니다:

```python
# 1. 모델에 도구 바인딩
model_with_tools = model.bind_tools([get_weather])

# 2. 모델이 도구 호출 생성
messages = [{"role": "user", "content": "서울의 날씨는 어때?"}]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

# 3. 도구 실행 및 결과 수집
for tool_call in ai_msg.tool_calls:
    tool_result = get_weather.invoke(tool_call)
    messages.append(tool_result)

# 4. 결과를 모델에 다시 전달하여 최종 응답 생성
final_response = model_with_tools.invoke(messages)
print(final_response.content)
```

## 3. 체인 (Chains)

체인은 여러 구성 요소를 순차적으로 연결하여 복잡한 워크플로우를 만드는 방법입니다. 하지만 LangChain v1.0에서는 **에이전트**를 사용하는 것이 더 권장됩니다.

### 간단한 체인 예제

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    ("user", "{input}")
])

# 체인 구성
chain = prompt | model

# 실행
response = chain.invoke({"input": "안녕하세요!"})
print(response.content)
```

## 4. 에이전트 (Agents)

에이전트는 LLM이 도구를 사용하여 작업을 수행할 수 있게 해주는 시스템입니다. 에이전트는 사용자의 요청을 받아, 필요한 도구를 선택하고 실행하며, 결과를 바탕으로 최종 답변을 생성합니다.

### 에이전트의 동작 방식

1. **사용자 입력 수신**: 사용자의 질문이나 요청을 받습니다.
2. **도구 선택**: LLM이 어떤 도구를 사용해야 할지 결정합니다.
3. **도구 실행**: 선택된 도구를 실행합니다.
4. **결과 분석**: 도구 실행 결과를 분석합니다.
5. **최종 응답 생성**: 필요하면 추가 도구를 호출하거나, 최종 답변을 생성합니다.

### create_agent를 사용한 간단한 에이전트

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# 도구 정의
@tool
def get_weather(city: str) -> str:
    """특정 도시의 날씨를 조회합니다."""
    return f"{city}의 날씨는 맑음입니다."

# 모델 초기화
model = ChatOpenAI(model="gpt-3.5-turbo")

# 에이전트 생성
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="당신은 날씨 정보를 제공하는 도우미입니다."
)

# 에이전트 실행
response = agent.invoke({
    "messages": [{"role": "user", "content": "서울의 날씨는 어때?"}]
})

print(response["messages"][-1].content)
```

## 핵심 개념 간의 관계

```
사용자 입력
    ↓
에이전트 (Agent)
    ↓
모델 (Model) → 도구 선택
    ↓
도구 (Tools) 실행
    ↓
결과를 모델에 전달
    ↓
최종 응답 생성
```

## 다음 단계

이제 핵심 개념을 이해했으니, 다음 섹션에서 에이전트를 더 자세히 살펴보고 ReAct 패턴을 학습하겠습니다.

