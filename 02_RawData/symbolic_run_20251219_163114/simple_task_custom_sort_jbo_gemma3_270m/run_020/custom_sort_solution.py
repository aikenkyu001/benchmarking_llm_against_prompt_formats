def custom_sort(string_list):
    """
    Sorts a list of strings in a custom way.

    Args:
        string_list: A list of strings.

    Returns:
        A new list containing the sorted strings.
    """
    try:
        sorted_list = sorted(string_list)
        return sorted_list
    except Exception as e:
        print(f"Error sorting the list: {e}")
        return string_list  # Return the original list if an error occurs