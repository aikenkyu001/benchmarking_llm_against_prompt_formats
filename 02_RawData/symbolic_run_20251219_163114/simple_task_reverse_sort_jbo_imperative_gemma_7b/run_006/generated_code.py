def reverse_sort(number_list):
    """
    Funkcija za obratno sortiranje liste brojeva.

    Parametari:
        number_list (list): Lista brojeva.

    Povratni rezultat:
        list: Obratno sortirana lista brojeva.
    """

    # Obratite sortu listu brojeva.
    number_list.sort(reverse=True)

    # Vrati obratno sortiranu listu brojeva.
    return number_list