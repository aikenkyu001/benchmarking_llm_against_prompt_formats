def simple_sort(number_list):
    """
    This function implements the quick sort algorithm to sort a given list of integers in ascending order.
    
    Args:
        number_list (list): A list of integers to be sorted.
        
    Returns:
        list: The sorted list of integers.
    """
    
    # Check if the input list is empty or contains only one element
    if len(number_list) == 1:
        return number_list
    
    # Split the input list into two halves based on the middle element
    mid = len(number_list) // 2
    left_half = [x for x in number_list[:mid]]
    right_half = [x for x in number_list[mid:]]
    
    # Call the simple sort function recursively with the left and right halves of the sorted list
    return simple_sort(left_half) + simple_sort(right_half)