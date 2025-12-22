def solve_puzzle():
    # Define the sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Pall Mall": ["Blends"], "Dunhill": ["Blends"], "Bluemaster": [], "Prince": []}

    # Define the backtracking function
    def backtrack(house_index, pet):
        if house_index == 2:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality for nationality in nationalities if nationality != pet) or \
                not any(drink for drink in drinks if drink != "Tea" and drink != pet) or \
                not any(smoke for smoke in smokes if smoke != pet):
                return True
        for i, color in enumerate(colors):
            if color == pet:
                # Constraint 2: The Swede keeps Dogs as pets.
                if any(nationality for nationality in nationalities if nationality != pet) or \
                    any(pet for pet in pets if pet != color) or \
                    any(drink for drink in drinks if drink != "Tea" and drink != color) or \
                    any(smoke for smoke in smokes_adj[color] if smoke != pet):
                    return True
        return False

    # Solve the puzzle using backtracking
    for i, house_index in enumerate(house_numbers):
        if backtrack(house_index, None):
            solution[i] = {"nationality": nationalities[pet], "drink": drinks[pet], "smokes": smokes_adj[color]}
            print(solution[i]["nationality"])
            return

# Call the solve_puzzle function
solve_puzzle()