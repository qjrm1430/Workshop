import unittest


# unittest에서는 테스트 클래스가 unittest.TestCase를 상속해야 합니다.
class TestMathFunctions(unittest.TestCase):
    # 테스트 메서드는 'test_'로 시작해야 합니다.
    def test_add(self):
        # 'self.assertEqual(a, b)'와 같은 전용 assert 메서드를 사용해야 합니다.
        self.assertEqual(2 + 3, 5)
        self.assertEqual(-1 + 1, 0)

    def test_subtract(self):
        self.assertEqual(10 - 5, 5)
        self.assertEqual(5 - 5, 0)


# 이 파일을 직접 실행할 경우를 위한 구문
if __name__ == "__main__":
    unittest.main()
