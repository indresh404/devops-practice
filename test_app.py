import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        print("Result:", result)   
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()