def copy_list(input_list):
    return input_list.copy()
```
This function takes an input list as an argument, and returns a complete copy of that list. The `copy()` method creates a new list object and initializes it with the elements from the original list, without modifying the original list.

Here's an example usage:
```
>>> original_list = [1, 2, 3]
>>> copied_list = copy_list(original_list)
>>> original_list
[1, 2, 3]  # still unchanged!
>>> copied_list
[1, 2, 3]  # a new list with the same elements
```
Note that this implementation uses the `copy()` method, which is available for lists in Python. This method creates a shallow copy of the list, meaning it only copies the references to the original elements, rather than recursively copying all nested objects. If you need a deep copy (i.e., a copy that also recursively copies nested objects), you can use the `copy.deepcopy()` function from the `copy` module:
```
import copy

def copy_list(input_list):
    return copy.deepcopy(input_list)