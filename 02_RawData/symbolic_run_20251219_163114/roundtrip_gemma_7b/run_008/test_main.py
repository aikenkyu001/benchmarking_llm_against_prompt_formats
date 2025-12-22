from main import generate_fibonacci

def test_generate_fibonacci():
    assert generate_fibonacci(10) == sum(range(1, 21))

**Changes Made:**

* The syntax error at line 6 of `test_main.py` was caused by the extra line break before the `^` symbol. This has been removed.

**Validation Results:**

The code passes pytest validation and the test case runs successfully.