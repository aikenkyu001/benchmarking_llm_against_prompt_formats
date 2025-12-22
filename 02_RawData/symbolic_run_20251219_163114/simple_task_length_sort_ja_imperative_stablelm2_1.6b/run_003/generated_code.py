def length_sort(string_list):
    # 列挙組み
    key = lambda x: len(x)
    
    # キューに新しいリストを持てる
    sorted_list = sorted(
        string_list, key=key
    )
    
    return sorted_list[::-1]  # 後ろから順番に並べて、末の元に戻す

# Test the function
print(length_sort(["apple", "banana", "cherry"]))