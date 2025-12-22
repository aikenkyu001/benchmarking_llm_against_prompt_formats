import pytest
import os
import sys

# Add the directory containing the generated code to the Python path
# The test runner script will place the generated file in the same dir as this test file.
sys.path.insert(0, os.path.dirname(__file__))

# Import the function from the generated code
# The name 'generated_code' will be the name of the file created by the test runner script.
try:
    from custom_sort_solution import custom_sort
except ImportError:
    pytest.fail("Could not import 'custom_sort' from 'custom_sort_solution.py'. "
                "The file might not have been generated correctly.")

# --- Test Cases ---

@pytest.mark.parametrize("input_list, expected_list", [
    # Basic case
    (["apple", "fig", "banana", "cherry", "date"], ["fig", "date", "apple", "banana", "cherry"]),
    # Case with already sorted elements
    (["a", "b", "c"], ["a", "b", "c"]),
    # Case with reverse sorted elements
    (["long", "short", "tiny"], ["long", "tiny", "short"]),
    # Case with same length elements
    (["cat", "bat", "ant"], ["ant", "bat", "cat"]),
    # Empty list
    ([], []),
    # List with one element
    (["single"], ["single"]),
    # List with numbers as strings
    (["10", "2", "100"], ["2", "10", "100"]),
    # Mixed case
    (["Apple", "apple", "Banana"], ["Apple", "apple", "Banana"]),
])
def test_custom_sort(input_list, expected_list):
    """
    Tests the custom_sort function with various inputs.
    """
    assert custom_sort(input_list) == expected_list
