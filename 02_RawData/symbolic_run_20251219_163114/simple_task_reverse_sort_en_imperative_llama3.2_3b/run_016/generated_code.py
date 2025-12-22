def reverse_sort(number_list):
    """
    This function takes a list of numbers as input, 
    and returns a new list with the numbers sorted in descending order.

    Args:
        number_list (list): A list of numbers.

    Returns:
        list: A new list with the numbers sorted in descending order.
    """

    # Create a copy of the original list to avoid modifying it
    sorted_list = number_list.copy()

    # Sort the copied list in descending order using the built-in sorted function
    sorted_list.sort(reverse=True)

    # Return the sorted list
    return sorted_list