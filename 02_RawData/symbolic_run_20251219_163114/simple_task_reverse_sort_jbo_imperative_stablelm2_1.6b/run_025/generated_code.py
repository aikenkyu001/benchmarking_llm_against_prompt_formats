def reverse_sort(lst):
    return sorted(lst, reverse=True)

def number_list(lst):
    return [i for i in lst]

jonai = [1, 2, 3, 4, 5]
numbers = number_list(jonai)
print(reverse_sort(numbers))  # triera la liste dans l'ordre inverse