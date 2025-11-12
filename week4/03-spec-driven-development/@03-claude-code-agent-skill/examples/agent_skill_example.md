# Claude Code Agent Skill 사용 예제

## 예제 1: 간단한 함수 생성

### 명세

```
함수: validate_email

목적: 이메일 주소의 유효성을 검증합니다.

입력:
  - email: str - 검증할 이메일 주소

출력:
  - bool - 유효하면 True, 그렇지 않으면 False

동작:
  1. @ 기호가 정확히 하나 있는지 확인
  2. @ 앞부분(로컬 부분)이 비어있지 않은지 확인
  3. @ 뒷부분(도메인)이 비어있지 않은지 확인
  4. 도메인에 점(.)이 있는지 확인
  5. 도메인의 마지막 부분(TLD)이 2자 이상인지 확인

예외:
  - email이 None이거나 빈 문자열이면 False 반환

예제:
  validate_email("user@example.com")  # True
  validate_email("invalid.email")      # False
  validate_email("")                   # False
```

### Agent Skill을 통한 생성 결과

```python
import re
from typing import Optional

def validate_email(email: Optional[str]) -> bool:
    """
    이메일 주소의 유효성을 검증합니다.
    
    Args:
        email: 검증할 이메일 주소
        
    Returns:
        유효하면 True, 그렇지 않으면 False
    """
    if not email:
        return False
    
    # @ 기호가 정확히 하나 있는지 확인
    if email.count("@") != 1:
        return False
    
    local_part, domain = email.split("@")
    
    # 로컬 부분이 비어있지 않은지 확인
    if not local_part:
        return False
    
    # 도메인이 비어있지 않은지 확인
    if not domain:
        return False
    
    # 도메인에 점이 있는지 확인
    if "." not in domain:
        return False
    
    # TLD가 2자 이상인지 확인
    tld = domain.split(".")[-1]
    if len(tld) < 2:
        return False
    
    return True
```

## 예제 2: 클래스 생성

### 명세

```
클래스: UserManager

목적: 사용자 관리를 담당하는 클래스입니다.

속성:
  - users: List[User] - 사용자 목록

메서드:
  1. add_user(name: str, email: str) -> User
     - 사용자를 추가합니다.
     - 이메일 중복 체크
     - User 객체 생성 및 반환
     
  2. get_user(user_id: int) -> User | None
     - ID로 사용자를 조회합니다.
     - 없으면 None 반환
     
  3. delete_user(user_id: int) -> bool
     - 사용자를 삭제합니다.
     - 성공하면 True, 실패하면 False

예외:
  - add_user: 이메일 중복 시 ValueError
  - get_user: user_id가 음수면 ValueError
  - delete_user: user_id가 음수면 ValueError
```

### Agent Skill을 통한 생성 결과

```python
from typing import List, Optional

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email

class UserManager:
    """
    사용자 관리를 담당하는 클래스입니다.
    """
    
    def __init__(self):
        self.users: List[User] = []
        self._next_id = 1
    
    def add_user(self, name: str, email: str) -> User:
        """
        사용자를 추가합니다.
        
        Args:
            name: 사용자 이름
            email: 사용자 이메일
            
        Returns:
            생성된 User 객체
            
        Raises:
            ValueError: 이메일이 중복된 경우
        """
        # 이메일 중복 체크
        if any(user.email == email for user in self.users):
            raise ValueError(f"이메일 '{email}'은 이미 사용 중입니다.")
        
        # User 객체 생성
        user = User(self._next_id, name, email)
        self.users.append(user)
        self._next_id += 1
        
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """
        ID로 사용자를 조회합니다.
        
        Args:
            user_id: 사용자 ID
            
        Returns:
            User 객체 또는 None
            
        Raises:
            ValueError: user_id가 음수인 경우
        """
        if user_id < 0:
            raise ValueError("user_id는 양수여야 합니다.")
        
        for user in self.users:
            if user.id == user_id:
                return user
        
        return None
    
    def delete_user(self, user_id: int) -> bool:
        """
        사용자를 삭제합니다.
        
        Args:
            user_id: 삭제할 사용자 ID
            
        Returns:
            성공하면 True, 실패하면 False
            
        Raises:
            ValueError: user_id가 음수인 경우
        """
        if user_id < 0:
            raise ValueError("user_id는 양수여야 합니다.")
        
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        
        return False
```

## 예제 3: API 엔드포인트 생성

### 명세

```
API 엔드포인트: POST /api/tasks

목적: 새로운 작업을 생성합니다.

요청:
  {
    "title": str,        # 필수, 1-200자
    "description": str,  # 선택, 최대 1000자
    "priority": str      # 선택, "low", "medium", "high" 중 하나
  }

응답:
  {
    "id": int,
    "title": str,
    "description": str | None,
    "priority": str,
    "status": str,       # 항상 "pending"
    "created_at": str    # ISO 8601 형식
  }

에러:
  - 400: 잘못된 요청 (title이 없거나 200자 초과, priority가 유효하지 않음)
  - 500: 서버 오류

예제:
  요청:
    {
      "title": "새 작업",
      "description": "작업 설명",
      "priority": "high"
    }
  
  응답:
    {
      "id": 1,
      "title": "새 작업",
      "description": "작업 설명",
      "priority": "high",
      "status": "pending",
      "created_at": "2024-01-01T00:00:00Z"
    }
```

### Agent Skill을 통한 생성 결과

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

app = FastAPI()

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="작업 제목")
    description: Optional[str] = Field(None, max_length=1000, description="작업 설명")
    priority: Optional[str] = Field("medium", description="우선순위")
    
    @validator("priority")
    def validate_priority(cls, v):
        if v not in ["low", "medium", "high"]:
            raise ValueError("priority는 'low', 'medium', 'high' 중 하나여야 합니다.")
        return v

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: str
    created_at: str

tasks_db = []
next_id = 1

@app.post("/api/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    """
    새로운 작업을 생성합니다.
    """
    global next_id
    
    try:
        new_task = TaskResponse(
            id=next_id,
            title=task.title,
            description=task.description,
            priority=task.priority,
            status="pending",
            created_at=datetime.utcnow().isoformat() + "Z"
        )
        
        tasks_db.append(new_task)
        next_id += 1
        
        return new_task
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")
```

## 팁

1. **명세를 단계적으로 작성**: 복잡한 기능은 여러 단계로 나누어 작성
2. **예제를 충분히 제공**: 구체적인 예제가 많을수록 더 정확한 코드 생성
3. **에러 케이스 명시**: 예외 상황을 명확히 기술
4. **피드백 반영**: 생성된 코드를 검토하고 명세를 개선

