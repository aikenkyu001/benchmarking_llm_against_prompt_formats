def reverse_sort(number_list):
    """
    Sorts the numbers in the input list in descending order and returns the sorted list.

    Parameters:
    number_list (list): A list of numbers to be sorted.

    Returns:
    list: A new list with the numbers from `number_list` sorted in descending order.
    """
    return sorted(number_list, reverse=True)