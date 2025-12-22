def reverse_sort(number_list):
    """
    Reverses the order of the elements in the `number_list`

    Args:
        number_list (list): The list of numbers to reverse.

    Returns:
        None
    """

    # Create a copy of the list so we don't modify it in place.
    reversed_list = copy.deepcopy(number_list)

    # Reverse the order of the elements in the `reversed_list`
    reversed_list.reverse()

    # Return the reversed list
    return reversed_list