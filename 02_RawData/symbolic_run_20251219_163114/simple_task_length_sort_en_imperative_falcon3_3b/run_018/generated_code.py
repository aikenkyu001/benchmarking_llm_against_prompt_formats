def length_sort(string_list):
    """
    Sorts a list of strings in ascending order based on their length.

    Parameters:
    string_list (list): A list of strings to be sorted.

    Returns:
    list: A new list with the strings from `string_list` sorted by length in ascending order.
    """
    return sorted(string_list, key=len)