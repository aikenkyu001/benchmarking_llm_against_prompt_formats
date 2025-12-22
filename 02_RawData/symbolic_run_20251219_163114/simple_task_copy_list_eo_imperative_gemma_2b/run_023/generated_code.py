def copy_list(input_list):
    """
    Kopion ekzaktan kopion de `input_list`. La originala listo ne devas esti modifita.

    Args:
        input_list (list): Lista de elementos.

    Returns:
        None
    """

    # Crea copia da lista
    copy_list = input_list.copy()

    # Deleta o elemento original da lista
    del input_list

    # Retorna a copia da lista
    return copy_list