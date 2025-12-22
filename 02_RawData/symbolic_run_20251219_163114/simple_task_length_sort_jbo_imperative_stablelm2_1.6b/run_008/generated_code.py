def length_sort(lst):
    # Cette fonction prend une liste comme argument
    lst = list(lst)  # Convertir la liste en un seul élément pour éviter les TypeError

    # Créer une nouvelle liste avec les tailles des éléments de la première liste
    sorted_lst = [len(item) for item in lst]

    # Supprimer les éléments du tableau 'sorted_lst' qui ont une taille égale à la taille de leur premier élément
    sorted_lst = [i for i in sorted_lst if i != len(lst[0])]

    return sorted_lst

# Exemple d'utilisation :
my_list = ['apple', 'banana', 'cherry', 'date']
print(length_sort(my_list))  # Vérifier que la fonction marche bien