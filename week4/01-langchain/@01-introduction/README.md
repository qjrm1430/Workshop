# LangChain 소개

## LangChain이란?

LangChain은 LLM(Large Language Model)을 활용하여 에이전트와 애플리케이션을 구축하기 위한 프레임워크입니다. **10줄 미만의 코드**로 OpenAI, Anthropic, Google 등 다양한 LLM 제공자와 연결할 수 있으며, 사전 구축된 에이전트 아키텍처와 모델 통합을 제공합니다.

## LangChain v1.0의 주요 특징

LangChain v1.0은 프로덕션 환경에서 사용할 수 있는 안정적이고 집중된 프레임워크입니다. 주요 특징은 다음과 같습니다:

### 1. 표준 모델 인터페이스

다양한 LLM 제공자들은 각각 고유한 API와 응답 형식을 가지고 있습니다. LangChain은 모델과 상호작용하는 방식을 표준화하여, 제공자를 쉽게 교체할 수 있고 벤더 종속성을 피할 수 있습니다.

### 2. 사용하기 쉬운 유연한 에이전트

LangChain의 에이전트 추상화는 **10줄 미만의 코드**로 간단한 에이전트를 만들 수 있도록 설계되었습니다. 동시에 원하는 모든 컨텍스트 엔지니어링을 수행할 수 있는 충분한 유연성도 제공합니다.

### 3. LangGraph 기반 구축

LangChain의 에이전트는 LangGraph 위에 구축되어 있습니다. 이를 통해 LangGraph의 **durable execution**(지속 가능한 실행), **human-in-the-loop**(사람 개입) 지원, **persistence**(영속성) 등의 기능을 활용할 수 있습니다.

### 4. LangSmith를 통한 디버깅

복잡한 에이전트 동작을 깊이 있게 시각화할 수 있는 도구를 제공합니다. 실행 경로를 추적하고, 상태 전환을 캡처하며, 상세한 런타임 메트릭을 제공합니다.

## LangChain vs LangGraph

언제 LangChain을 사용하고, 언제 LangGraph를 사용해야 할까요?

### LangChain을 사용하는 경우

- 빠르게 에이전트와 자율 애플리케이션을 구축하고 싶을 때
- 일반적인 LLM 및 도구 호출 루프를 위한 사전 구축된 아키텍처가 필요할 때
- 높은 수준의 추상화를 원할 때

### LangGraph를 사용하는 경우

- 결정론적(deterministic) 워크플로우와 에이전트 워크플로우의 조합이 필요할 때
- 높은 수준의 커스터마이징이 필요할 때
- 지연 시간을 세밀하게 제어해야 할 때

**중요**: LangChain 에이전트는 LangGraph 위에 구축되어 있으므로, 기본적인 LangChain 에이전트 사용을 위해서는 LangGraph를 직접 알아야 할 필요는 없습니다.

## LangChain v1.0의 주요 변경사항

### create_agent: 새로운 표준

v1.0에서는 `create_agent`가 에이전트를 구축하는 표준 방법이 되었습니다. 이전 버전의 `langgraph.prebuilt.create_react_agent`를 대체하며, 더 깔끔하고 강력한 API를 제공합니다.

### 표준 콘텐츠 블록

모든 제공자에서 최신 LLM 기능에 대한 통합 액세스를 제공하는 새로운 `content_blocks` 속성이 추가되었습니다.

### 간소화된 패키지

`langchain` 패키지는 에이전트 구축을 위한 필수 구성 요소에 집중하도록 간소화되었으며, 레거시 기능은 `langchain-classic`으로 이동되었습니다.

## 다음 단계

이제 LangChain의 기본 개념을 이해했으니, 다음 섹션에서 설치 및 환경 설정 방법을 알아보겠습니다.

