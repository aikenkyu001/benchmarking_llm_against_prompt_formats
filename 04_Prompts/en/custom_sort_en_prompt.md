You are a Python programmer. Please create Python code to custom sort a list according to the following instructions.

**Instructions:**

Implement a function named `custom_sort`.
This function takes a list of strings `string_list` as an argument.
The function should return a new list sorted according to the following two rules:

1.  **Primary Rule**: Sort by the length of the string, with shorter strings coming first.
2.  **Secondary Rule**: If the lengths of the strings are the same, sort them in lexicographical (alphabetical) order.

**Output Format:**

Your response must consist only of a Python code block.
Do not include any explanation or comments other than the code.

**Example Input:**
`["apple", "fig", "banana", "cherry", "date"]`

**Expected Example Output:**
`["fig", "date", "apple", "banana", "cherry"]`
