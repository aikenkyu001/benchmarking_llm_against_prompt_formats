def length_sort(string_list):
    """
    Ordigas liston de stringoj laŭ longeco.

    Args:
        string_list (list): Listo de stringoj.

    Returns:
        list: Nova listo de stringoj ordigitaj laŭ kreska ordo de ilia longeco.
    """
    return sorted(string_list, key=len)