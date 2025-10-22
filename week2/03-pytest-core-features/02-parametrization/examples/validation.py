# validation.py

import re

def is_valid_email(email: str) -> bool:
    """
    주어진 문자열이 기본적인 이메일 형식을 따르는지 확인합니다.
    - '@' 기호가 하나만 있어야 합니다.
    - '@' 뒤에 '.'이 하나 이상 있어야 합니다.
    - 너무 간단한 정규식을 사용하므로 완벽하지는 않습니다.
    """
    if not isinstance(email, str):
        return False
    
    # 간단한 이메일 형식 검사를 위한 정규 표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return re.match(pattern, email) is not None

def check_password_strength(password: str) -> str:
    """
    비밀번호의 강도를 평가합니다.
    - 8자 미만: '매우 약함'
    - 8자 이상, 숫자 미포함: '약함'
    - 8자 이상, 숫자 포함: '강함'
    """
    if not isinstance(password, str):
        raise TypeError("비밀번호는 문자열이어야 합니다.")

    if len(password) < 8:
        return '매우 약함'
    
    if not any(char.isdigit() for char in password):
        return '약함'
        
    return '강함'
