# LangChain 설치 및 환경 설정

## 사전 요구사항

- Python 3.10 이상
- `uv` 패키지 관리자 (이 워크샵에서는 `uv`를 사용합니다)

## 설치 방법

### 1. 기본 LangChain 패키지 설치

LangChain의 핵심 패키지를 설치합니다:

```bash
uv add langchain
```

### 2. 모델 제공자 패키지 설치

LangChain은 다양한 LLM 제공자와의 통합을 위해 독립적인 제공자 패키지를 사용합니다. 사용하려는 제공자에 맞는 패키지를 설치해야 합니다.

#### OpenAI 사용 시

```bash
uv add langchain-openai
```

#### Anthropic (Claude) 사용 시

```bash
uv add langchain-anthropic
```

#### Google 사용 시

```bash
uv add langchain-google-genai
```

### 3. 추가 통합 패키지 (선택사항)

필요에 따라 추가 통합 패키지를 설치할 수 있습니다:

```bash
# 벡터 스토어, 임베딩 등 커뮤니티 통합
uv add langchain-community

# LangSmith (디버깅 및 모니터링)
uv add langsmith
```

## 환경 변수 설정

대부분의 LLM 제공자는 API 키를 환경 변수로 설정해야 합니다.

### OpenAI API 키 설정

```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your-api-key-here"

# Windows CMD
set OPENAI_API_KEY=your-api-key-here

# Linux/Mac
export OPENAI_API_KEY="your-api-key-here"
```

### Anthropic API 키 설정

```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY="your-api-key-here"

# Windows CMD
set ANTHROPIC_API_KEY=your-api-key-here

# Linux/Mac
export ANTHROPIC_API_KEY="your-api-key-here"
```

### .env 파일 사용 (권장)

프로젝트 루트에 `.env` 파일을 생성하고 환경 변수를 설정할 수 있습니다:

```env
OPENAI_API_KEY=your-api-key-here
ANTHROPIC_API_KEY=your-api-key-here
```

Python에서 `.env` 파일을 사용하려면 `python-dotenv` 패키지를 설치하고 로드해야 합니다:

```bash
uv add python-dotenv
```

```python
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경 변수 로드
```

## 간단한 테스트

설치가 제대로 되었는지 확인하기 위해 간단한 테스트를 해봅시다:

```python
from langchain_openai import ChatOpenAI

# 모델 초기화
model = ChatOpenAI(model="gpt-3.5-turbo")

# 간단한 호출 테스트
response = model.invoke("안녕하세요!")
print(response.content)
```

## week4 워크샵 환경 설정

이 워크샵에서는 `week4/pyproject.toml`에 필요한 모든 패키지가 정의되어 있습니다. 다음 명령어로 한 번에 설치할 수 있습니다:

```bash
cd week4
uv sync --dev
```

이 명령어는 다음 패키지들을 설치합니다:
- `langchain`: LangChain 핵심 패키지
- `langgraph`: LangGraph (LangChain 에이전트가 내부적으로 사용)
- `langchain-openai`: OpenAI 통합
- `langchain-anthropic`: Anthropic 통합
- `langchain-community`: 커뮤니티 통합

## 다음 단계

설치가 완료되었으니, 다음 섹션에서 LangChain의 핵심 개념(모델, 체인, 에이전트, 도구)을 알아보겠습니다.

