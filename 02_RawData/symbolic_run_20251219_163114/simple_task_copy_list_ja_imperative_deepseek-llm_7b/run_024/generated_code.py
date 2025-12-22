def copy_list(input_list):
    # リスト要素ごとに対応する配列を作成
    copied_list = []
    
    # 元のリストの要素数分ループ
    for i in range(len(input_list)):
        # 現在の要素値を保持したいた形で追加
        copied_list.append(input_list[i])
    
    return copied_list