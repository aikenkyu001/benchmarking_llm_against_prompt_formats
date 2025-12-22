def copy_list(input_list):
    """
    This function takes a list as input and returns a new list containing a complete copy of the original list. The original list is not modified in any way.
    
    :param input_list: a list to be copied
    :return: a new list containing a complete copy of the original list
    """
    # create a copy of the input list
    copy_list = [item for item in input_list]
    
    # return the new list
    return copy_list