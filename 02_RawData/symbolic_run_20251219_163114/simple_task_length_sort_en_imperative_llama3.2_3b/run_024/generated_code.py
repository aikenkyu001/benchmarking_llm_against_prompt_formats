def length_sort(string_list):
    """
    This function takes a list of strings as input, sorts them in ascending order based on their length, and returns the sorted list.

    Args:
        string_list (list): A list of strings to be sorted by length.

    Returns:
        list: A new list with the strings from `string_list` sorted in ascending order based on their length.
    """
    # Use the built-in sorted function to sort the list
    # The key argument specifies that we want to sort based on the length of each string
    return sorted(string_list, key=len)