def length_sort(string_list):
    # 文字列の長さを格納するリスト
    string_lengths = [len(x) for x in string_list]
    
    # 短い順に並べ替え、長さと結合した新しいリストを作成
    sorted_strings = [[x, y] for y, x in sorted(enumerate(string_lengths), key=lambda v: v[1])]
    
    return sorted_strings