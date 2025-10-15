# 📊 uv 성능 벤치마크

이 페이지에서는 `uv`와 Python 생태계의 다른 도구들의 성능을 비교합니다.

모든 벤치마크는 실제 프로젝트인 [Trio](https://github.com/python-trio/trio)의 의존성을 기준으로 측정되었습니다. 각 그래프에서 **막대가 작을수록(시간이 짧을수록) 더 좋은 성능**을 의미합니다.

---

### 1. 패키지 설치 (Installation)

가상 환경에 패키지를 설치하는 속도를 비교합니다. (`uv pip sync`와 유사한 작업)

#### 웜 캐시(Warm Cache) 설치

이미 한 번 이상 설치하여 캐시가 남아있는 상태에서, 가상 환경을 지우고 다시 설치하는 경우입니다.

![Warm Installation](https://github.com/user-attachments/assets/84118aaa-d030-4e29-8f1e-9483091ceca3)

#### 콜드 캐시(Cold Cache) 설치

캐시가 전혀 없는 새로운 환경(예: CI 서버, 새 PC)에서 처음으로 패키지를 설치하는 경우입니다.

![Cold Installation](https://github.com/user-attachments/assets/e7f5b203-7e84-452b-8c56-1ff6531c9898)

---

### 2. 의존성 해결 (Resolution)

`requirements.in` 파일로부터 `requirements.txt`와 같은 잠금(lock) 파일을 생성하는 속도를 비교합니다. (`uv pip compile`과 유사한 작업)

#### 웜 캐시(Warm Cache) 의존성 해결

캐시는 있지만 잠금 파일이 없는 상태에서, 의존성 관계를 처음부터 다시 분석하는 경우입니다.

![Warm Resolution](https://github.com/user-attachments/assets/e1637a08-8b27-4077-8138-b3849e53eb04)

#### 콜드 캐시(Cold Cache) 의존성 해결

캐시가 전혀 없는 새로운 환경에서 의존성 관계를 분석하는 경우입니다.

![Cold Resolution](https://github.com/user-attachments/assets/b578c264-c209-45ab-b4c3-54073d871e86)

---

-   **출처**: [uv 공식 벤치마크 문서](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)

