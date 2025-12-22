def length_sort(lst):
    # Cette fonction prend une liste comme argument
    lst = list(lst)  # Convertir la liste en un seul élément pour éviter les TypeError

    # Créer une nouvelle liste avec les tailles des éléments de la liste originale
    sorted_lst = [len(item) for item in lst]

    # Remplacer les tailles des éléments dans la liste originale par leur valeur réelle
    lst[:] = sorted_lst

# Exemple d'utilisation :
my_list = ['apple', 'banana', 'cherry']
length_sort(my_list)
print(my_list)  # Voulez-vous manger cette pomme, ce noyau ou ce fruit de la passion ?