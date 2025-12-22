def custom_sort(string_list):
    """
    Ordigas liston de ĉenoj laŭ la longo de la ĉeno,
    kun pli mallongaj ĉenoj unue. Se la longoj estas samaj,
    ordigu ilin laŭ leksikografia (alfabeta) ordo.
    """
    return sorted(string_list, key=lambda x: (len(x), x))