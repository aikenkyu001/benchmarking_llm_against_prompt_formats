def solve_puzzle():
    # Step 1: Identify the position of houses
    positions = [1, 2, 3, 4, 5]

    # Step ..
    # Use logical reasoning to assign nationality to each house

    # Step 3: Infer information that can be derived indirectly by combining constraints
    for i in range(4):
        next_house_position = (positions[i] + 1) % 5
        if positions[i] + 1 == 2:
            continue
        constraint_index = 6 - ((next_house_position - 1) // 3)
        if positions[i] + 1 == 9 and constraint_index == 7:
            return "German"

    # If no German owner is found, return None
    return None

# Example usage
print(solve_puzzle())