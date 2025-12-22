import unittest
from . import generate_fibonacci as gf

class TestGenerateFibonacci(unittest.TestCase):
    def test_gf(self):
        self.assertEqual(gf(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])