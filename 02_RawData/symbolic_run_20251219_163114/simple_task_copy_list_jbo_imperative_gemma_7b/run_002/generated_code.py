def copy_list(input_list):
    """
    Funkcija koja kopira listu.

    Parametari:
        input_list: Unutrašnja lista.

    Povratni rezultat:
        Nova lista koja sadrži iste elemente kao i unutrašnja lista.
    """

    output_list = []
    for element in input_list:
        output_list.append(element)

    return output_list