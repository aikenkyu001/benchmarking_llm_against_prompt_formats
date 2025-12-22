from generated_code import simple_sort
def test_simple_sort_basic():
    assert simple_sort([3, 1, 2]) == [1, 2, 3]
def test_simple_sort_empty():
    assert simple_sort([]) == []
def test_simple_sort_negative():
    assert simple_sort([-1, -5, 0]) == [-5, -1, 0]