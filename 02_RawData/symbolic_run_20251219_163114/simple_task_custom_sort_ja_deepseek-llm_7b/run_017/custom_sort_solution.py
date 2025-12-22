def custom_sort(string_list):
    # 文字列の長さでソート
    string_list.sort(key=len)
    
    # 辞書順にソート
    string_list.sort()
    
    return string_list