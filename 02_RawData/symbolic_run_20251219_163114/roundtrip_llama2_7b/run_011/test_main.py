import unittest
from main import generating_fibonacci

class TestGenerateFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        self.assertEqual(generating_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
Note that I've also corrected the import statement in `test_main.py` to use the correct module name.