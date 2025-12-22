def reverse_sort(number_list):
    new_list = []
    for num in number_list:
        if num > 0:
            new_list.append(num)
        else:
            break
    return new_list

number_list = [1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(reverse_sort(number_list)))