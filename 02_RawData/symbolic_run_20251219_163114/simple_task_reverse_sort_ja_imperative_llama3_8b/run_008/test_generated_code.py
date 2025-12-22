from generated_code import reverse_sort
def test_reverse_sort_basic():
    assert reverse_sort([3, 1, 2]) == [3, 2, 1]
def test_reverse_sort_empty():
    assert reverse_sort([]) == []