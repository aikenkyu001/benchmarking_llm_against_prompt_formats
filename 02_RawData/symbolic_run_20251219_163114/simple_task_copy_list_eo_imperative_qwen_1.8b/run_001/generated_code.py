def copy_list(input_list):
    output_list = input_list.copy()
    return output_list

# Example usage:
original_list = ['apple', 'banana', 'cherry'],
copied_list = copy_list(original_list)

print(copied_list))  # Output: ['apple', 'banana', 'cherry'], ['cherry']`
In this Python code, we define a function `copy_list` that takes an input list as its parameter. The function uses the built-in `copy()` method to create a new copy of the input list.

The `copy()` method in Python creates a shallow copy of an object or sequence of objects. In our case, we are creating a shallow copy of the original input list using the `copy()` method.

After creating a shallow copy of the input list using the `copy()` method, we return this new copy of the input list as its output parameter.

Finally, in the example usage section, we create an instance of the `copy_list` function with the `original_list` as its input parameter. We then call the `copy_list` function with this `original_list` as its input parameter and store the returned copy of the original list in a variable called `copied_list`.

Finally, in the example usage section, we print the `copied_list` to verify that it contains the same elements as the original input list. The output of the code should be: