def custom_sort(string_list):
    """
    Sorts a list of strings based on length and lexicographical order.

    Args:
        string_list: A list of strings.

    Returns:
        A new list sorted according to the specified rules.
    """
    return sorted(string_list, key=lambda x: (len(x), x))