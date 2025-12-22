import λ
from λ import λ_generate_fibonacci

def test_generate_fibonacci():
    assert λ_generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

---