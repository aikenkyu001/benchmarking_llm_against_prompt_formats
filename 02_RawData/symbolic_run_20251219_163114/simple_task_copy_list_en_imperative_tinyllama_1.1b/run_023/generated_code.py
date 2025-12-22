def copy_list(input_list):
    """
    This function creates a copy of the given input list and returns it.
    
    Args:
        input_list (list): The original list to be copied.
        
    Returns:
        list: A copy of the given input list.
    """
    # Create a new empty list to store the copy
    output_list = []
    
    # Iterate through each element in the input list and add it to the output list
    for item in input_list:
        output_list.append(item)
        
    return output_list