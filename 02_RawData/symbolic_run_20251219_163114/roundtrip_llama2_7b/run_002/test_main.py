import unittest
from main import generating_fibonacci

class TestGenerateFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        self.assertEqual(generating_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
---
Now, the test should pass without any errors.