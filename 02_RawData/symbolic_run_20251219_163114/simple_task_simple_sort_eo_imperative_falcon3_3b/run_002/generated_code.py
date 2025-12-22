def simple_sort(number_list):
    """
    This function sorts a list of numbers in ascending order using a simple sorting algorithm.

    Parameters:
    number_list (list): A list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    for i in range(len(number_list)):
        min_index = i
        for j in range(i+1, len(number_list)):
            if number_list[min_index] > number_list[j]:
                min_index = j
        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]
    return number_list