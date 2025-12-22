def copy_list(input_list):
    # Make a deep copy of input_list using the deepcopy() function from the copy module
    import copy
    
    # Use the copy.deepcopy() function to create a new list that is an exact copy of input_list
    copied_list = copy.deepcopy(input_list)
    
    # Return the copied list without modifying the original input_list
    return copied_list