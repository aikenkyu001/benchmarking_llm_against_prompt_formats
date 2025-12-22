def copy_list(input_list, output_list):
    # 関数名: `copy_list`
    input_list = input_list.split(',')
    
    # 処理: `input_list` の完全なコピーを返せ.元のリストは変更してはならない。
    output_list = []
    
    # 遍历输入列表
    for i in range(len(input_list))):
        # 将当前元素添加到输出列表中
        output_list.append(i)
    
    return output_list