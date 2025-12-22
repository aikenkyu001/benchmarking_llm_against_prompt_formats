def reverse_sort(number_list):
    # Sort function with a key that will be the negative of the original number
    sorted_list = sorted(number_list, key=lambda x: -x)
    
    return sorted_list[::-1]