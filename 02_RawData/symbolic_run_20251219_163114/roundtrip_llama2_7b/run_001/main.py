python
import unittest
from . import generafibonacci

class TestGenerateFibonacci(unittest.TestCase):
    def test_generafibonacci(self):
        self.assertEqual(generafibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])