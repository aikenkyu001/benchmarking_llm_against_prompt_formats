def length_sort(string_list):
    """
    Sorts a list of strings in lexicographical order.

    Args:
        string_list (list[str]): A list of strings.

    Returns:
        list[str]: A sorted list of strings.
    """
    # Convert the list of strings to a list of tuples, where each tuple contains a string and its length
    string_tuples = [(string, len(string))) for string in string_list]

    # Sort the list of tuples using the `sorted()` function with the `key` parameter set to a lambda function that returns the length of each tuple
    sorted_string_tuples = sorted(string_tuples, key=lambda x: x[1]))[:len(string_list))]

    return sorted_string_tuples