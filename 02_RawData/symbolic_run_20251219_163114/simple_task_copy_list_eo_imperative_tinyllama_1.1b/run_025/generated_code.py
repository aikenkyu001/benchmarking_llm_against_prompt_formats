def copy_list(input_list):
    """
    Copies the elements of a given list `input_list` to a new list.
    
    Args:
        input_list (list): The list to be copied.
        
    Returns:
        list: A new list with the same elements as `input_list`.
    """
    # Create a copy of the input list
    output_list = [item for item in input_list]
    
    return output_list