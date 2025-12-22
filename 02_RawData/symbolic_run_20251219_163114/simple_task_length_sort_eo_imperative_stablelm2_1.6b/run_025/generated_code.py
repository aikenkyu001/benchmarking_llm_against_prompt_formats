def length_sort(string_1: list) -> list:
    """
    Sorts a list of strings by their lengths.

    Parameters:
        string_1(list): A list of strings.

    Returns:
        list: The sorted list.
    """
    return sorted(string_1, key=len)