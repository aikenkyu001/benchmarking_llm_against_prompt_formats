def reverse_sort(number_list):
    # Create a new list with the numbers from `number_list` sorted in **Descending** order.
    new_list = []
    for number in number_list:
        if number < 0:
            new_list.append(-number)
        else:
            new_list.append(number)
    
    return new_list