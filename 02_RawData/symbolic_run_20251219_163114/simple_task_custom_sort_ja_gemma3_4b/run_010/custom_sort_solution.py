def custom_sort(string_list):
    """
    文字列のリストを、長さでソートし、長さが同じ場合は辞書順にソートします。

    Args:
        string_list: ソートする文字列のリスト。

    Returns:
        ソートされた新しいリスト。
    """
    return sorted(string_list, key=lambda x: (len(x), x))