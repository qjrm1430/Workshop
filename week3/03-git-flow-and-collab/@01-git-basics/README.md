# 01. Git 기초: 버전 관리의 첫걸음

Git은 소스 코드의 **변경 이력**을 기록하고, 협업을 돕는 도구입니다.

## 핵심 개념
- 커밋(commit): 스냅샷
- 브랜치(branch): 작업 줄기
- 머지(merge)/리베이스(rebase): 변경 통합 방식
- 원격(remote): GitHub 등

## 주요 명령어
```bash
git init
git status
git add .
git commit -m "feat: initial commit"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

## 미니 실습
1. 로컬 폴더에서 `git init`
2. 파일 생성 후 `git add`, `git commit`
3. GitHub 리포지토리 생성 후 `remote` 연결, `push`
