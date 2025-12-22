def reverse_sort(number_list):
    """
    number_list の数値を降順にソートした新しいリストを返します。

    引数:
        number_list: 数値のリスト

    戻り値:
        sorted_list: 数値を降順にソートしたリスト
    """

    sorted_list = sorted(number_list, reverse=True)
    return sorted_list