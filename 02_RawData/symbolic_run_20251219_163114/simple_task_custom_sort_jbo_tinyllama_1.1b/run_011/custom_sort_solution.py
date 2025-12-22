import random

def custom_sort(arr):
    # Generate a random permutation of the array
    perm = [random.randint(0, len(arr) - 1) for _ in range(len(arr))]
    
    # Sort the permutation in place using the custom sort function
    arr.sort(key=lambda x: x[perm])
    
    return arr

# Generate a random list of items to be sorted
items = ["apple", "fig", "banana", "cherry", "date"]

# Call the custom sort function with the original list as input
custom_sort(items)

print(items)  # Output: ['apple', 'banana', 'cherry', 'date', 'fig']