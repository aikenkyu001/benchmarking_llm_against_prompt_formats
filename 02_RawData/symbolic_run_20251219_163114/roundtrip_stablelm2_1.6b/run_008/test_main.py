import pytest

def test_generate_fibonacci_call():
    assert (
        (lambda-Test call to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

def test_generate_fibonacci_4args():
    assert (
        (lambda-Test call to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

def test_generate_fibonacci_5args():
    assert (
        (lambda-Test call
         to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

def test_generate_fibonacci_7args():
    assert (
        (lambda-Test call
         to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

# Transpiled Python code files for the S-expression script

main.py:python
def generate_fibonacci(count):
    result = 0
    a = 0
    b = 1
    _ = count(κ, "count")
    sum_plus_result = result + sum([a, b])
    a, b = b, a + b
    _ = count(κ, "a")
    sum_minus_one = result - ..
    _ = count(κ, "b")
    sum_plus_two = sum_plus_result + b
    a, b = b, a + b
    _ = count(κ, "temp")
    return a

def main():
    result = generate_fibonacci(ι, "count")
    print(result)

if __name__ == "__main__":
    main()

test_main.py:python
import pytest

def test_generate_fibonacci_call():
    assert (
        (lambda-Test call to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

def test_generate_fibonacci_4args():
    assert (
        (lambda-Test call to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

def test_generate_fibonacci_5args():
    assert (
        (lambda-Test call to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

def test_generate_fibonacci_7args():
    assert (
        (lambda-Test call to generate_fibonacci)
        == sum([0, 1, 1, 2, 3, 5, 8])
    )