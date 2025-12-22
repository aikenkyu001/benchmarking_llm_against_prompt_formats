def length_sort(string_list):
    # 遍历字符串列表
    for string in string_list:
        # 将字符串转换为长度
        length = len(string)
        
        # 如果长度小于当前的长度，将其添加到新的列表中
        if length < current_length:
            new_list.append(current_length + length))
    
    return new_list