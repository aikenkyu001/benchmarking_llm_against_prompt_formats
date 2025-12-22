from generated_code import copy_list
def test_copy_list_basic():
    l = [1, 2, 3]
    c = copy_list(l)
    assert c == l
    assert id(c) != id(l)
def test_copy_list_empty():
    assert copy_list([]) == []