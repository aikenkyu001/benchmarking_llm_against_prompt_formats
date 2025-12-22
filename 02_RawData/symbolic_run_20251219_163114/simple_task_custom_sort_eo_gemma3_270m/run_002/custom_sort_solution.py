def custom_sort(string_list):
    """
    Realigu funkcion nomitan `custom_sort`.
    Ĉi tiu funkcio akceptas liston de ĉenoj `string_list` kiel argumenton.
    La funkcio devus redoni novan liston ordigitan laŭ la sekvaj du reguloj:
    1.  **Unua Regulo**: Ordigi laŭ la longo de la ĉeno, kun pli mallongaj ĉenoj unue.
    2.  **Dua Regulo**: Se la longoj de la ĉenoj estas samaj, ordigu ilin laŭ leksikografia (alfabeta) ordo.
    """
    try:
        sorted_list = sorted(string_list)
        return sorted_list
    except Exception as e:
        print(f"Error: {e}")
        return []