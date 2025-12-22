def simple_sort(number_list):
    """
    Simple sorting function that sorts a list of numbers in ascending order.

    Args:
        number_list (list): A list of numbers to be sorted.

    Returns:
        list: A new list with the numbers from number_list sorted in ascending order.
    """

    # Iterate over the list and sort the numbers.
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            if number_list[i] > number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]

    # Return the sorted list.
    return number_list