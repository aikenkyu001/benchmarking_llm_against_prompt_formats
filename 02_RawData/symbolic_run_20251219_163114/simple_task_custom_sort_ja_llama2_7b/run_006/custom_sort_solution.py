def custom_sort(string_list):
    # 第一ルール：文字列の長さでソート
    sorted_list = sorted(string_list, key=len)
    
    # 第二ルール：文字列の長さが同じ場合は、辞書順にソート
    sorted_list = sorted(sorted_list, key=lambda x: x[1])
    
    return sorted_list