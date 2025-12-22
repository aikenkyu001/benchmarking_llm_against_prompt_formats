import unittest

def test_generate_fibonacci():
    call = lambda: generate_fibonacci(κ, "count")
    expected_result = [0, 1, 1, 2, 3, 5, 8]
    result = list(map(lambda x: sum(x), call))
    self.assertEqual(result, expected_result)

if __name..
    unittest.main()