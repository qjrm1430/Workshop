# 05. Conventional Commits: 의미있는 기록을 남기는 법

커밋 메시지 구조:
```
<type>(<scope>): <subject>

<body>

<footer>
```
- `type`: feat, fix, docs, style, refactor, test, chore
- `scope`: 변경 범위(선택)
- `subject`: 간결한 명령문
- `body`: 이유/세부 내용
- `footer`: BREAKING CHANGE, 이슈 참조 등

## 예시
```
feat(auth): add login API
fix(ui): correct button alignment
refactor(core): extract validation utility
```

브레이킹 변경:
```
feat(api)!: rename /users to /members

BREAKING CHANGE: clients must update endpoint
```

**😍 제목(header)과 본문(body)을 빈행으로 분리**

- 커밋 유형 이후 제목과 본문은 한글로 작성하여 내용이 잘 전달될 수 있도록 할 것
- 본문에는 변경한 내용과 이유 설명
- 어떻게보다는 무엇(What) & 왜(Why)를 설명

**⚠️ 한 커밋에는 한 가지 문제만!**

- 추적 가능하게 유지해주기
- 너무 많은 문제를 한 커밋에 담으면 추적하기 어렵다.

# Commit 기본 구조

```
<type><is breakchange(!)>: <subject> // 제목
<BLANK LINE> // 구분줄\n
<body>       // 내용
```

## 제목(header)

```
<type><is breakchange(!)>: <subject> // 제목
```

### 커밋 유형: `<type>`

| 커밋 유형 | 의미 |
| --- | --- |
| `Feat` | 새로운 기능 추가 |
| `Fix` | 버그 수정 |
| `Docs` | 문서 수정 |
| `Style` | 코드 formatting, 세미콜론 누락, 코드 자체의 변경이 없는 경우 |
| `Refactor` | 코드 리팩토링 |
| `Test` | 테스트 코드, 리팩토링 테스트 코드 추가 |
| `Chore` | 관리(maintain), 핵심 내용은 아닌 잡일 등 패키지 매니저 수정, 그 외 기타 수정 ex) .gitignore |
| `Design` | CSS 등 사용자 UI 디자인 변경 |
| `Comment` | 필요한 주석 추가 및 변경 |
| `Rename` | 파일 또는 폴더 명을 수정하거나 옮기는 작업만인 경우 |
| `Remove` | 파일을 삭제하는 작업만 수행한 경우 |
| `!BREAKING CHANGE` | 커다란 API 변경의 경우 |
| `!HOTFIX` | 급하게 치명적인 버그를 고쳐야 하는 경우 |

### **브레이크 체인지 여부**: `<is breakchange>`

💡 기존 개발하는 방식에 비해 많이 변경된 경우를 알리기 위한 표시. 또한, 브레이크 체인지가 존재하는 경우 변경내용에 대한 설명을 body에 작성

- type뒤에 ‘!’ 추가
- 예시
    - `feat!: 랭킹 점수 계산 공식 변경`
        
        ```
        feat!: 랭킹 점수 계산 공식 변경
        
        원래 해당 계산식을 사용했었지만
        이런 공식으로 코드가 수정되었습니다.
        ```
        
    - `feat: 로그인 기능 구현`

### **제목 내용**: `<subject>`

- 명령조로 작성
- 현재 시제 사용
- 끝에 . 없이 작성

## 바디: `<body>`

- 커밋에 대한 동기와 이전 코드와의 대조를 설명
- 여러가지 항목이 있다면 글머리 기호( - )를 통해 가독성 높이기
- 현재 시제 사용
- 기본은 선택 사항
- 브레이크 포인트가 존재하는 경우, 반드시 변경 사항의 설명을 body에 명시할 것

## 예제

```
feat: 경매품 업로드 기능 구현
```

```
feat!: 랭킹 점수 계산식 변경

기존 계산식은 기여 `횟수 * 영상 시간(분)`이었지만, 기획 변경으로 인해 `횟수 * 영상 시간(초)`로 변경되었습니다.
이슈 사항 : https://github.com/proact0/act1/server/issues/1
```

## CLI에서 커밋 메시지 여러 줄로 작성하는 방법

✅ **쌍따옴표를 닫지 말고 개행하며 작성 → 다 작성한 후에 쌍따옴표를 닫으면 작성 완료**

```bash
git commit -m "FEAT: 회원가입 기능 추가

- 회원가입 기능 추가"
```

![Untitled](media\1.png)

## 규칙에 맞는 좋은 커밋메시지를 작성해야 하는 이유

- 팀원과의 소통
- 편리하게 과거 추적 가능
- 나중에 실무에서 익숙해지기 위해

☝ 안지킨 사례

![Untitled](media\2.png)

☝ 지킨 사례

![Untitled](media\3.png)

# 이슈(Issue)

- 담당자(Assignees)를 명시 할 것
- Task list 기능을 적극 활용할 것
- 기능에 관련된 Issue라면 Github Project와 PR(PullRequest)과 연동하여 진행상황을 공유할 것
    
    ![1111.png](media\4.png)
    

# Pull Request

- 제목은 '[기능 | 기능 번호] 변경 사항' 구조로 작성할 것
- Issue와 연동할 것
- 예시
    
    ![1111.png](media\5.png)