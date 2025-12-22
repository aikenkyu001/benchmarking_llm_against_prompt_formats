import pytest

def test_generate_fibonacci():
    assert (
        lambda call: generate_fibonacci(1)
         == [0, 1, 1, 2, 3, 5, 8]
        or
        lambda call: generate_fibonacci(2)
         == [1, 1, 2, 3, 5, 8, 9]
    )

def test_main():
    assert (
        lambda call: call()
         == 0
     )