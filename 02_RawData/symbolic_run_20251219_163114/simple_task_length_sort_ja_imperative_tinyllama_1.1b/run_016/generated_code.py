def lengtth_sort(string_list):
    """
    Sorts a list of strings in descending order based on their lengths.
    
    Args:
        string_list (list): A list of strings to be sorted.
        
    Returns:
        List: The sorted list of strings.
    """
    
    # Convert the input list to a set for faster sorting
    string_set = set(string_list)
    
    # Sort the set in descending order based on length
    return sorted(string_set, key=len, reverse=True)