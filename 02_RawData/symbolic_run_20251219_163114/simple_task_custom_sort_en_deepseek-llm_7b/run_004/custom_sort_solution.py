def custom_sort(string_list):
    return sorted(string_list, key=len)

# Test the function with given input
input_list = ["apple", "fig", "banana", "cherry", "date"]
output_list = custom_sort(input_list)
print(output_list)