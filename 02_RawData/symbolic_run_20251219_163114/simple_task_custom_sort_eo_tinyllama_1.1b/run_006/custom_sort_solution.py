import string

def custom_sort(string_list):
    """
    Sorts a list of strings by length in alphabetical order.
    
    Args:
        string_list (list[str]): A list of strings to be sorted.
        
    Returns:
        List[str]: The sorted list of strings.
    """
    
    # Define the unsorted list of strings
    unsorted_string_list = [s for s in string_list if len(s) > 1]
    
    # Sort the unsorted list by alphabetical order
    return sorted(unsorted_string_list, key=lambda x: len(x))