def custom_sort(string_list):
    # 第一规则：根据字符串长度进行排序
    sorted_list = sorted(string_list, key=len)))
    
    # 第二规则：如果字符串长度相同，则按照字典顺序进行排序
    if len(sorted_list)) > 1:
        sorted_list.sort(key=str.lower))
    
    return sorted_list

# 示例
string_list = ["apple", "fig", "banana", "cherry", "date"]]
sorted_list = custom_sort(string_list)
print(sorted_list)