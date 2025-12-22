import copy

# Stvaranje dva lista
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:] # koristimo `copy()` za kopiranje liste
print(f"Originalni list: {original_list}")
print(f"Kopirana lista: {copied_list}")