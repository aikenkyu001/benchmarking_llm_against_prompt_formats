def copy_list(input_list):
    return input_list.copy()
```
This function takes a list as input, and returns a shallow copy of that list. The `copy()` method creates a new list with the same elements as the original list, without modifying the original list.

Note: If you want to create a deep copy (i.e., a copy of the entire structure, including any nested lists or objects), you can use the `copy.deepcopy()` function from the `copy` module:
```
import copy

def copy_list(input_list):
    return copy.deepcopy(input_list)