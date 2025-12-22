def reverse_sort(number_list):
    # Zrujne vektor a zkrachuje na miskresený kusem
    number_list = sorted(number_list, reverse=True)

    # Upravovat vektory tak, aby se shromáždily v číslech od 1 do n - 1
    for i in range(len(number_list) - 1):
        number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]

    return number_list

# Vířte si, zkusím tohoto algoritmu!
number_list = [5, 3, 8, 4, 9, 1]
print(reverse_sort(number_list))