def solve_puzzle():
    # Define the puzzle as a list of dictionaries.
    houses = [
        {"color": "red", "nationality": "Brit", "beverage": "tea", "cigarette": "Dane", "pet": "dog"},
        {"color": "green", "nationality": "Swede", "beverage": "coffee", "cigarette": "Pall Mall", "pet": "cat"},
        {"color": "white", "nationality": "Dane", "beverage": "milk", "cigarette": "Norwegian", "pet": "horse"},
        {"color": "blue", "nationality": "German", "beverage": "beer", "cigarette": "Prince", "pet": "horse"},
        {"color": "yellow", "nationality": "Swede", "beverage": "coffee", "cigarette": "Dunhill", "pet": "cat"},
    ]

    # Define the backtrack function.
    def backtrack(current_assignment):
        if len(current_assignment) == 5:
            return current_assignment

        for i in range(1, 6):
            new_assignment = {**current_assignment[i-1], **{k: v for k, v in houses[i]}}
            result = backtrack(new_assignment)
            if isinstance(result, str):  # Constraint satisfaction.
                return result
            else:
                current_assignment[i-1].update(result)

        return "No solution"

    # Call the backtrack function with an initial assignment that satisfies all constraints.
    result = backtrack(houses)
    if isinstance(result, str):
        print("No solution")
    else:
        print(f"{result['nationality']}")

# Run the solve_puzzle function to find a solution.
solve_puzzle()