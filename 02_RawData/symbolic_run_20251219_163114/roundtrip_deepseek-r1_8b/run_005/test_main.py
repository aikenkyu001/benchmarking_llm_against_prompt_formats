from main import generate_fibonacci

def test_generate_fibonacci():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    actual = generate_fibonacci(10)
    assert actual == expected, f"Expected {expected}, got {actual}"