def copy_list(input_list):
    """
    Creates an exact copy of the input list.

    Args:
        input_list (list): The list to be copied.

    Returns:
        list: A copy of the input list.
    """

    # Create a new list to store the copy.
    copied_list = []

    # Iterate over the input list and add each element to the copied list.
    for element in input_list:
        copied_list.append(element)

    # Return the copied list.
    return copied_list