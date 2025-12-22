def reverse_sort(number_list):
    """
    number_list を降順にソートした新しいリストを返します。

    Args:
        number_list (list): 数字のリスト

    Returns:
        list: number_list の数値を降順にソートした新しいリスト
    """
    # 1番から最後まで繰り返し処理を行う
    for i in range(len(number_list)):
        # 最後の要素から始めて、各要素とその次の要素を比較する
        for j in range(len(number_list) - 1):
            if number_list[j] < number_list[j + 1]:
                # 2つの数字が逆になっている場合、入れ替える
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    return number_list