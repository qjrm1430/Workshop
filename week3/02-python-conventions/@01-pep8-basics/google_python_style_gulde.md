참조 : ([Google Python Style Guide](https://yosseulsin-job.github.io/Google-Python-Style-Guide-kor/), PEP8)

# ☑️ 코드 컨벤션

## 네이밍 가이드라인

| 타입 | 네이밍 | Example |
| --- | --- | --- |
| 패키지 | snake_case | lower_with_under |
| 모듈 | snake_case | lower_with_under |
| 클래스 | PascalCase | CapWords |
| 예외(Exception) | PascalCase | CapWords |
| 함수 | snake_case | lower_with_under() |
| 상수 | UPPER_CASE | CAPS_WITH_UNDER |
| 변수 | snake_case | lower_with_under |
| 메서드 | snake_case | lower_with_under() |
| 함수/메서드 매개변수 | snake_case | lower_with_under |

<aside>
<img src="https://cdn-icons-png.flaticon.com/512/7350/7350737.png" alt="https://cdn-icons-png.flaticon.com/512/7350/7350737.png" width="40px" /> **문자열을 처리할 때는 쌍따옴표를 사용하도록 합니다.**

</aside>

### 피해야 하는 이름

- 아래와 같은 특별한 경우를 제외한 단일 글자는 피한다.
    - counters이나 iterators에서 사용할 때 (예. `i`, `j`, `k`, `v` 등)
    - `try/except`문에서 예외 식별자로 `e`를 사용할 때

## 문자열 포매팅

- 문자열 포매팅(format)을 할 때 f-string 포매팅을 사용한다.
- 이유
    - %Operator, str.format, f-string 3가지의 포매팅 속도를 비교하였을 때 f-string 속도가 가장 빠르다.
    - 표현식을 직접 평가하여 문자열에 삽입하기 때문에 추가적인 파싱이나 변환 작업 없이 직접적인 문자열 생성이 가능하다.
- f 접두사를 붙여 사용

```python
name = 'Proact0'
print(f"Project : {name}")
# 출력 : "Project : Proact0"
```

## 매개변수 및 반환값 타입 어노테이션

> 상세설명 참조 : https://yosseulsin-job.github.io/Google-Python-Style-Guide-kor/#s3.19
> 
- 추후 수정이 불필요한 확정적으로 사용되는 타입들은 필히 명시
- 반환값이 None인 경우에는 `→ None` 타입 명시 필수