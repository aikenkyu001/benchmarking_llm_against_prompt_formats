def custom_sort(string_list):
    # 1. Unua Regulo: Ordenigo laŭ longo de la ĉeno
    string_list.sort(reverse=True, key=len)

    # 2. Dua Regulo: Ordenigo laŭ leksikografia (alfabeta) ordo
    if len(string_list) > 1:
        string_list.sort(key=lambda x: x if x.isalpha() else ord(x))

    return string_list