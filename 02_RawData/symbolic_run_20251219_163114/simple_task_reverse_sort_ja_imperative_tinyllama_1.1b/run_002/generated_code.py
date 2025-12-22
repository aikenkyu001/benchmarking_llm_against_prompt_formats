def reversesort(number_list):
    # define the sorted list
    sorted_list = []
    
    # loop through each element in the input list
    for num in number_list:
        # if the current element is less than the previous one, add it to the sorted list
        if num < number_list[len(number_list)-1]:
            sorted_list.append(num)
    
    return sorted_list