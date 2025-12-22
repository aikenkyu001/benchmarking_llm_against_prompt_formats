def length_sort(string_list):
    # 入力引数を受け取り
    list_lengths = [len(s) for s in string_list]
    # 長さが短い順に並べ替える
    sorted_list = sorted(string_list, key=lambda x: list_lengths.index(x))
    # 新しいリストを返す
    return sorted_list