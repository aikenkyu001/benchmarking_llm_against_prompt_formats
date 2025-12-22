def reverse_sort(number_list):
    """
    Returns a new list with the numbers from number_list sorted in descending order.

    Args:
        number_list (list): A list of numbers.

    Returns:
        list: A new list with the numbers from number_list sorted in descending order.
    """

    # Sort the numbers in descending order
    number_list.sort(reverse=True)

    # Return the sorted list
    return number_list