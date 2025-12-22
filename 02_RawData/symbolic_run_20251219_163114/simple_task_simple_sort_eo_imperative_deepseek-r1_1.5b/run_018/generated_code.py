def simple_sort(number_list):
    # Oronde la lista de números en orden descendiente
    sorted_numbers = sorted(number_list, reverse=True)
    # Revolver la lista para obtener la ordenada en orden ascendiente
    ordered_numbers = sorted(sorted_numbers)
    return ordered_numbers

# Luego, usaremos la función simple_sort para ordenar una lista
number_list = input("Enter a list of numbers: ")
sorted_number_list = simple_sort(number_list)

print("The sorted list is:", sorted_number_list)