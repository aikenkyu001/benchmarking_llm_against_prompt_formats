def copy_list(input_list):
    # Use slicing to create a shallow copy of input_list
    return input_list[:]

# Test the function
original_list = [1, 2, 3, 4, 5]
copied_list = copy_list(original_list)

print("Original List: ", original_list)
print("Copied List: ", copied_list)

# Modify the copied list
copied_list.append(6)

print("After modifying copied list: ", copied_list)