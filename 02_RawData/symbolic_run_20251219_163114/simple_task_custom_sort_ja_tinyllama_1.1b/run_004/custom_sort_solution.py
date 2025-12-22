def custom_sort(string_list):
    # Implement custom sort based on first and second rules
    
    # Sort by length in descending order
    string_list.sort(key=lambda s: len(s), reverse=True)
    
    # Convert to dictionary sorted alphabetically
    return {k: v for k, v in zip(*sorted(string_list))}