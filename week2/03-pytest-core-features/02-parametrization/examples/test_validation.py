# test_validation.py
import pytest
from validation import is_valid_email, check_password_strength

# === is_valid_email 함수 테스트 ===

@pytest.mark.parametrize("email, expected", [
    # --- 유효한 케이스들 ---
    ("test@example.com", True),
    ("user.name@domain.co.kr", True),
    ("user123@sub.domain.org", True),
    
    # --- 유효하지 않은 케이스들 ---
    ("test@example", False),          # TLD (최상위 도메인) 없음
    ("user@.com", False),             # 도메인 이름 없음
    ("user@", False),                 # 도메인 전체 없음
    ("@example.com", False),          # 사용자 이름 없음
    ("user name@example.com", False), # 중간에 공백 포함
    ("user@example..com", False),     # 연속된 점 포함
    (12345, False),                   # 문자열이 아닌 입력
])
def test_is_valid_email(email, expected):
    """다양한 케이스에 대해 이메일 유효성 검사를 테스트합니다."""
    assert is_valid_email(email) == expected

# === check_password_strength 함수 테스트 ===

@pytest.mark.parametrize("password, expected_strength", [
    # --- 매우 약함 케이스 ---
    ("1234567", "매우 약함"),
    ("short", "매우 약함"),
    ("", "매우 약함"),

    # --- 약함 케이스 ---
    ("longpassword", "약함"),
    ("withoutdigit", "약함"),
    
    # --- 강함 케이스 ---
    ("strongpass123", "강함"),
    ("123password", "강함"),
    ("has1number", "강함"),
])
def test_check_password_strength(password, expected_strength):
    """다양한 비밀번호에 대해 강도 평가를 테스트합니다."""
    assert check_password_strength(password) == expected_strength

def test_check_password_strength_invalid_type():
    """정수가 입력되었을 때 TypeError가 발생하는지 테스트합니다."""
    with pytest.raises(TypeError):
        check_password_strength(12345678)
