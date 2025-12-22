from main import generate_fibonacci

def test_generate_fibonacci():
    expected = 34
    result = generate_fibonacci(10)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_ = test_generate_fibonacci()

# End of files