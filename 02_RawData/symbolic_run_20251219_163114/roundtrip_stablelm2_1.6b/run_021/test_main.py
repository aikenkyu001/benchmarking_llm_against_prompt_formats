import pytest
from main import generate_fibonacci

def test_generate_fibonacci():
    assert (
        (lambda call: generate_fibonacci(κ, "count"))
        == sum([0, 1, 1, 2, 3, 5, 8])
    )

@pytest.mark.runtest
def run_test():
    from main import generate_fibonacci
    result = generate_fibonacci(κ, "count")
    assert result == pytest.approx(55)

if __name__ == "__main__":
    test_generate_fibonacci()
    run_test()