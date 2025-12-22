from main import generate_fibonacci
import unittest

class TestFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        expected = [0, 1]
        self.assertEqual(generate_fibonacci(), expected)

if __name__ == '__main__':
    unittest.main()