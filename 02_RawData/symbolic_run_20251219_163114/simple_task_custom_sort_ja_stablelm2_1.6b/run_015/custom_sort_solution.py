def custom_sort(string_list):
    # 第一ルール: 文字列の長さでソート
    string_list.sort(key=len)
    
    # 第二ルール: 文字列の長さが同じ場合は、辞書順（アルファベット順）にソート
    for i in range(1, len(string_list)):
        if len(string_list[i]) < len(string_list[i-1]):
            string_list[i], string_list[i-1] = string_list[i-1], string_list[i]
            
    return string_list

# チェック用の例句
string_list = ["apple", "fig", "banana", "cherry", "date"]
sorted_list = custom_sort(string_list)
print(sorted_list)