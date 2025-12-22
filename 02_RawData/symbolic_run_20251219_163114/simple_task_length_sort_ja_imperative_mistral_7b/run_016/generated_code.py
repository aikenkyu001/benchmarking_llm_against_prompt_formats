def length_sort(string_list):
    # 文字列の長さを取得する関数
    def get_length(s):
        return len(s)

    # sorted() 関数で並べ替え、比較関数に get_length() を渡します。
    return sorted(string_list, key=get_length)