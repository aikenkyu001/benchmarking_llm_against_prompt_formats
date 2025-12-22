def simple_sort(number_list):
    """
    Sorts a list of numbers in ascending order using the quick sort algorithm.
    
    Args:
        number_list (list): A list of numbers to be sorted.
        
    Returns:
        list: The sorted list of numbers.
    """
    
    # Define the quicksort function
    def quicksort(arr, left, right):
        if left < right:
            # Choose a pivot element and partition the array around it
            pivot = arr[left]
            i = left
            j = right - 1
            
            while i <= j:
                while arr[i] < pivot and I < j:
                    I += 1
                while arr[j] > pivot and I >= j + 1:
                    j -= 1
                if I <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    I += 1
                    
            # Swap the pivot element with its corresponding element in the right half of the array
            arr[left], arr[right] = arr[right], arr[left]
            
            # Recursively sort the left and right halves of the array
            quicksort(arr, left, right - 1)
            quicksort(arr, right + 1, right)
        
    # Sort the input list using the quicksort algorithm
    sorted_list = []
    for num in number_list:
        if not quicksort(sorted_list, 0, len(number_list)-1):
            break
    
    return sorted_list