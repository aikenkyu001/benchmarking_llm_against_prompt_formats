from generated_code import length_sort
def test_length_sort_basic():
    assert length_sort(["a", "ccc", "bb"]) == ["a", "bb", "ccc"]
def test_length_sort_empty():
    assert length_sort([]) == []