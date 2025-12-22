def length_sort(string_list):
    """
    Sorts a list of strings in ascending order based on their length.

    Args:
        string_list: A list of strings.

    Returns:
        A new list with the strings from string_list sorted in ascending order based on their length.
    """
    try:
        sorted_list = sorted(string_list)
        return sorted_list
    except Exception as e:
        print(f"Error sorting the list: {e}")
        return []  # Return an empty list in case of an error