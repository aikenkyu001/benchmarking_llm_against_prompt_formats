def reverse_sort(number_list):
    """
    Kreu Python-funkcion.

    - Funkcia Nomo: `reverse_sort`
    - Eniga Parametro: `number_list`
    - Ago: Redonu novan liston kun la nombroj el `number_list` ordigitaj laŭ **malkreska** ordo.
    """

    # Ordini la liston laŭ malgrandaj ordoj.
    number_list.sort(reverse=True)

    # Returni la liston kun la nombroj ordigitaj laŭ malgrandaj ordoj.
    return number_list