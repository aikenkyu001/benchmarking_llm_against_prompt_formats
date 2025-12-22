def length_sort(string_list):
    """
    Sorts a list of strings based on their lengths in ascending order.

    Parameters:
    string_list (list): A list of strings to be sorted.

    Returns:
    list: The sorted list of strings based on their lengths.
    """
    return sorted(string_list, key=len)