def lengtth_sort(string_list):
    """
    This function takes a list of strings as input and returns a new sorted list with the strings in ascending order based on their length.
    
    :param string_list: A list of strings to be sorted.
    :return: A new sorted list with the strings in ascending order based on their length.
    """
    
    # Convert the input list to a set for faster sorting
    string_set = set(string_list)
    
    # Sort the set using the `sorted()` function
    return sorted(string_set, key=len)