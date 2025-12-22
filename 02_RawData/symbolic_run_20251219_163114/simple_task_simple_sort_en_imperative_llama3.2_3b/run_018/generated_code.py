def simple_sort(number_list):
    """
    This function takes a list of numbers as input, sorts them in ascending order and returns the sorted list.

    Args:
        number_list (list): A list of numbers to be sorted.

    Returns:
        list: A new list with the numbers from `number_list` sorted in ascending order.
    """

    # Create a copy of the original list to avoid modifying it
    sorted_list = number_list.copy()

    # Use the built-in sort function to sort the list in ascending order
    sorted_list.sort()

    # Return the sorted list
    return sorted_list