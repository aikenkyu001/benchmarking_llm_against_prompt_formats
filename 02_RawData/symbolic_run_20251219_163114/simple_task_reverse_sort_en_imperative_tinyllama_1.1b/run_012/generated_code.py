def reversesort(numbers):
    """
    This function takes a list of integers as input and returns a new sorted list.
    
    The function uses the reverse sort algorithm to sort the numbers in descending order.
    
    Args:
        numbers (list): A list of integers to be sorted.
        
    Returns:
        list: A new sorted list with the same elements as `numbers`.
    """
    
    # Create a copy of the input list
    sorted_numbers = [num for num in numbers]
    
    # Sort the original list using the reverse sort algorithm
    sorted_numbers.sort(reverse=True)
    
    return sorted_numbers