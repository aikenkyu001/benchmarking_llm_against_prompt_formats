def simple_sort(number_list):
    """
    number_list を昇順にソートした新しいリストを返します。

    Args:
        number_list (list): 数字のリスト

    Returns:
        list: number_list の数値を昇順にソートした新しいリスト
    """
    # 1番から最後まで繰り返しループで数字を比較する
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            # 2つの数字が等しい場合、次の数字に進む
            if number_list[i] == number_list[j]:
                continue
            # 1番目が大きい場合、交換する
            elif number_list[i] > number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]
    return number_list