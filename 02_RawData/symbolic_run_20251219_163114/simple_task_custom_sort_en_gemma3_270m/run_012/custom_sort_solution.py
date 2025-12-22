def custom_sort(string_list):
    """
    Sorts a list of strings according to the following two rules:
    1.  Sort by length, with shorter strings coming first.
    2.  If the lengths of the strings are the same, sort them in lexicographical (alphabetical) order.
    """
    if len(string_list) == 0:
        return []
    try:
        sorted_list = sorted(string_list)
        return sorted_list
    except Exception as e:
        print(f"Error sorting: {e}")
        return []