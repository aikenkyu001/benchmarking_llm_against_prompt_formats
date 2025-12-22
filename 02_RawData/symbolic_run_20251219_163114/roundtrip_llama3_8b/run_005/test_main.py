from main import generate_fibonacci

def test_generate_fibonacci():
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

These files should now pass the pytest validation.