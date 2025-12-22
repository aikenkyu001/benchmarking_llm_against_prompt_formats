def length_sort(string_list):
    # Zorguloj, ke la funkcio estas uzata por laŭ laŭ longo
    if not string_list:
        return None

    # Zorguloj, ke la funkcio estas uzata por laŭ laŭ longo
    if not isinstance(string_list, list):
        return None

    # Zorguloj, ke la funkcio estas uzata por laŭ laŭ longo
    if len(string_list) <= 1:
        return string_list

    # Zorguloj, ke la funkcio estas uzata por laŭ laŭ longo
    if not isinstance(string_list[0], str):
        return None

    # Zorguloj, ke la funkcio estas uzata por laŭ laŭ longo
    if not isinstance(string_list[1], str):
        return None

    # Ordoni la lista principe per laŭ laŭ longeco
    string_list.sort(key=len)

    # Degrupo la lista kaj return laŭa
    return string_list