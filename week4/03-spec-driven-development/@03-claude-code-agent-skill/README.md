# Claude Code - Agent Skill

## Claude Code란?

Claude Code는 Anthropic에서 개발한 AI 코딩 어시스턴트입니다. Claude Code는 자연어 명세를 이해하고, 그 명세를 바탕으로 코드를 생성할 수 있습니다.

## Agent Skill이란?

Agent Skill은 Claude Code가 **복잡한 작업을 여러 단계로 나누어 수행**할 수 있게 해주는 기능입니다. 단순히 코드를 생성하는 것을 넘어, 전체 개발 프로세스를 이해하고 실행할 수 있습니다.

## Agent Skill의 특징

### 1. 컨텍스트 이해

Agent Skill은 프로젝트의 전체 컨텍스트를 이해하고, 기존 코드와의 일관성을 유지합니다.

### 2. 단계별 실행

복잡한 작업을 여러 단계로 나누어 순차적으로 실행합니다:
- 요구사항 분석
- 설계
- 구현
- 테스트
- 리팩토링

### 3. 자동 검증

생성된 코드가 명세를 충족하는지 자동으로 검증합니다.

### 4. 반복 개선

초기 결과가 만족스럽지 않으면, 피드백을 바탕으로 개선합니다.

## Spec-driven Development와의 조합

Agent Skill은 Spec-driven Development와 매우 잘 맞습니다:

1. **명확한 명세 제공**: 명세가 명확할수록 더 정확한 코드 생성
2. **자동 구현**: 명세를 바탕으로 코드 자동 생성
3. **검증**: 생성된 코드가 명세를 충족하는지 확인
4. **반복 개선**: 명세를 수정하여 코드 개선

## 사용 예제

### 명세 작성

```
함수: fetch_user_profile

목적: 사용자 ID를 받아 사용자 프로필을 가져옵니다.

입력:
  - user_id: int - 사용자 ID

출력:
  - dict - 사용자 프로필
    {
      "id": int,
      "name": str,
      "email": str,
      "created_at": str
    }

동작:
  1. 데이터베이스에서 사용자 조회
  2. 사용자가 없으면 None 반환
  3. 사용자 정보를 딕셔너리로 변환하여 반환

예외:
  - user_id가 음수: ValueError("user_id는 양수여야 합니다")
  - 데이터베이스 연결 실패: DatabaseError("데이터베이스 연결에 실패했습니다")

예제:
  profile = fetch_user_profile(123)
  # 결과: {"id": 123, "name": "홍길동", "email": "hong@example.com", "created_at": "2024-01-01"}
```

### Agent Skill을 통한 코드 생성

명세를 Claude Code에 제공하면, Agent Skill이:
1. 명세를 분석
2. 필요한 의존성 확인
3. 코드 생성
4. 테스트 작성
5. 문서화

## Agent Skill 활용 팁

### 1. 명확한 명세 작성

명세가 명확할수록 더 정확한 코드가 생성됩니다.

### 2. 컨텍스트 제공

프로젝트의 전체 맥락을 제공하면 더 일관된 코드가 생성됩니다.

### 3. 점진적 개선

한 번에 완벽한 코드를 기대하지 말고, 반복적으로 개선합니다.

### 4. 검증 및 테스트

생성된 코드를 항상 검증하고 테스트합니다.

## 다음 단계

이제 Claude Code - Agent Skill을 이해했으니, 다음 섹션에서 Spec-driven Development의 전체 워크플로우를 알아보겠습니다.

