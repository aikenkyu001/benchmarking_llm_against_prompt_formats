def simple_sort(numbers):
    # Convert all elements to integers if possible
    try:
        sorted_numbers = sorted(int(x) for x in numbers)
    except ValueError:
        # If conversion fails, sort as strings or handle accordingly
        return sorted(numbers)
    return sorted_numbers

# Example usage:
numbers = ["1", "2", 3]
sorted_numbers = simple_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 3]