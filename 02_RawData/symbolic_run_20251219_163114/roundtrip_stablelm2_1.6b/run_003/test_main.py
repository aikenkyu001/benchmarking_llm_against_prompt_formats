python.
def test_generate_fibonacci():
    result = 0
    a = 0
    b = 1

    for _ in range(cook):
        result += a
        a, b = b, result + b
    assert generate_fibonacci(5) == result, "Test failed"

    print("All tests passed")