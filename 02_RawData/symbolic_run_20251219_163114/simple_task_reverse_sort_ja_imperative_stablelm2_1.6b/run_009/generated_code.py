def reverse_sort(number_list):
    # 副ノ制のソート
    number_list.sort(key=lambda x: -x)
    
    return number_list

# まだテストしていないが、以下は必要なテストを提供します。
print(reverse_sort([5, 3, 1, 4])) # [1, 3, 4, 5]
print(reverse_sort([-2, -1, 0, 1])) # [-1, 0, 1, -2]