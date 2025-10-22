# test_student_db.py
import pytest
from student_db import StudentDB


# `@pytest.fixture` 데코레이터를 사용하여 fixture를 정의합니다.
# 이 fixture는 테스트에 필요한 StudentDB 객체를 생성하고, 테스트가 끝난 후 정리합니다.
@pytest.fixture
def db():
    # --- 설정 (Setup) ---
    print("\n--- Fixture: 설정 시작 ---")
    db_instance = StudentDB()
    db_instance.connect("test_db")

    # `yield`를 사용하여 테스트 함수에 db_instance 객체를 전달합니다.
    # 테스트 함수의 실행은 이 시점에서 이루어집니다.
    yield db_instance

    # --- 정리 (Teardown) ---
    # 테스트 함수 실행이 끝나면 yield 다음 코드가 실행됩니다.
    print("--- Fixture: 정리 시작 ---")
    db_instance.close()


# 테스트 함수는 인자로 fixture 함수의 이름을 받습니다.
# 그러면 pytest가 해당 fixture를 실행하고 그 결과를 주입해줍니다.
def test_get_student_name_alice(db):
    print(">> test_get_student_name_alice 실행")
    student_name = db.get_student_name(1)
    assert student_name == "Alice"


def test_get_student_name_bob(db):
    print(">> test_get_student_name_bob 실행")
    student_name = db.get_student_name(2)
    assert student_name == "Bob"


def test_get_non_existent_student(db):
    print(">> test_get_non_existent_student 실행")
    student_name = db.get_student_name(99)
    assert student_name is None
