def lengtth_sort(string_list):
    """
    Sorts a list of strings in alphabetical order using the Lenient Sort algorithm.
    
    Args:
        string_list (list): A list of strings to be sorted.
        
    Returns:
        List: The sorted list of strings.
    """
    # Create a list of tuples containing the indices of each element in the original list
    indices = [(i, s) for I, s in enumerate(string_list)]
    
    # Sort the indices by their corresponding elements in the original list
    indices.sort()
    
    # Extract the sorted elements from the indices list and return them as a new list
    return [s[i] for i, s in indices]