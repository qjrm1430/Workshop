# student_db.py

class StudentDB:
    def __init__(self):
        self._data = {}

    def connect(self, db_name):
        print(f"'{db_name}' 데이터베이스에 연결합니다...")
        # 실제 DB 연결 대신 딕셔너리를 사용해 간단히 흉내 냅니다.
        self._data = {
            1: {'name': 'Alice', 'major': 'Computer Science'},
            2: {'name': 'Bob', 'major': 'Data Science'},
            3: {'name': 'Charlie', 'major': 'Mathematics'}
        }
        print("연결 성공.")

    def get_student_name(self, student_id):
        student = self._data.get(student_id)
        return student['name'] if student else None

    def close(self):
        print("데이터베이스 연결을 닫습니다...")
        self._data = {}
        print("연결 종료.")
