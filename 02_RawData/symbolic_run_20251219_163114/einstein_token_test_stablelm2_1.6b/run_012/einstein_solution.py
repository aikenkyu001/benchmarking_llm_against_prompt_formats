def solve_puzzle():
    # Define the sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Red": [], "Green": [], "Blue": []}
    drinks_adj = {"Tea": [], "Coffee": [], "Milk": [], "Beer": [], "Water": []}

    # Define the backtracking function
    def backtrack(house_index, pet):
        if house_index == 2:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality in smokes_adj for nationality in nationalities) or \
                not any(drink in drinks_adj for drink in drinks) or \
                not any(pet in pets for pet in pets):
                return True
        for i in range(len(house_numbers)):
            # Check if the current house is valid and assign the pet to it.
            if i == 0:
                smokes_adj[colors[i]] = [pet]
                drinks_adj[drink] = [smokes_adj[colors[i]].pop(0)]
                if solve(house_index + 1):
                    return True
                smokes_adj[colors[i]].pop(0)
            elif i != house_index:
                # Check if the pet is valid.
                if any(pet in pets for pet in pets) and \
                        not any(smoke in smokes_adj for smoke in smokes) or \
                        not any(drink in drinks_adj for drink in drinks):
                    return True
        return False

    # Solve the puzzle
    if backtrack(0, "Fish"):
        print("The Norwegian's nationality is:", nationalities[house_numbers.index(2)])
    else:
        print("No solution found.")

solve_puzzle()