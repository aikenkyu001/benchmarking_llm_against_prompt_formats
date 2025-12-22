def length_sort(string_list):
    """
    Sort a list of strings in ascending order based on their length.

    Args:
        string_list (list): A list of strings.

    Returns:
        list: A new list with the strings sorted in ascending order based on their length.
    """

    # Sort the strings based on their length.
    string_list.sort(key=len)

    # Return the sorted list.
    return string_list