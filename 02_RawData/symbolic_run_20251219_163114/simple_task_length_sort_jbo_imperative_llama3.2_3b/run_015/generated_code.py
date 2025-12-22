def length_sort(string_list):
    """
    Funkti'o ni fonksiyon ki'a velsi'a lo cnano liste poi se stika lo ka zancu'i lo lerfu **slunli**.
    
    Args:
        string_list (list): List of strings
    
    Returns:
        list: List of strings sorted by length
    """
    # Funkti'o cu zbasu lo `string_list` ki'a velsi'a lo cnano liste
    return sorted(string_list, key=len)