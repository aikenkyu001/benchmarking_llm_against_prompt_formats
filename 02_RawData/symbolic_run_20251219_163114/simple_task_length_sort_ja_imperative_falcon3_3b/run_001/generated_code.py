def length_sort(string_list):
    """
    Sort a list of strings in descending order based on their lengths.

    Args:
        string_list (list): A list of strings to be sorted.

    Returns:
        list: A new list with strings sorted by length in descending order.
    """
    return sorted(string_list, key=len, reverse=True)