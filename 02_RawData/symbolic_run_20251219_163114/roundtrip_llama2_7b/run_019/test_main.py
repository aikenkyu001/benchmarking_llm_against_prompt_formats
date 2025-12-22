import unittest
from main import generating_fibonacci

class TestGenerateFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        self.assertEqual(generating_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
With these changes, you should be able to run the test again without encountering any errors.