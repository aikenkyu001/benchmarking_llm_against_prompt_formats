python
import unittest
from . import generate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])