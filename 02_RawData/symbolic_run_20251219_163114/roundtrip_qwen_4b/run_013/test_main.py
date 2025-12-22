def test_generate_fibonacci():
    count = 10
    result = generate_fibonacci(count)
    assert result == [0, 1, 2, 3, 5, 8, 13, 21, 34)]


test_generate_fibonacci()