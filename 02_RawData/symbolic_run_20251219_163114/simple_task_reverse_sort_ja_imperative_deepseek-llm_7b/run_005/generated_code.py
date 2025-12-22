def reverse_sort(number_list):
    """
    引数で与えられた number_list の要素を逆順に並び替え、
    新しいリストを返却する関数。

    Args:
        number_list (List[int]): 降順にソートされるための整数リスト。

    Returns:
        リスト型: 引数で与えられた number_list を逆順に並び替えた新しいリスト。
    """
    
    # 降順にソートするためのコピーオブジェクト生成
    sorted_list = number_list.copy()
    sorted_list.reverse()

    return sorted_list