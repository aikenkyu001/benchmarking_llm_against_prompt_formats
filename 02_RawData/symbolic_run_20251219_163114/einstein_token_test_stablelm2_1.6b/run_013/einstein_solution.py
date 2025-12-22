def solve_puzzle():
    # Define the sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Pall Mall": ["Tea"], "Dunhill": ["Coffee"], "Blends": ["Milk"], "Bluemaster": ["Beer"], "Prince": ["Water"]}

    # Define the backtracking function
    def backtrack(house_index):
        if house_index == 2:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality in ["Brit", "Swede"] for nationality in smokes_adj.get("Brit")) or not any(drink in drinks for drink in smokes_adj.get("Swede") when drink != "Tea"):
                return True
            # Constraint 2: The Swede lives in house 2.
            if nationalities.index(nationality) != 1 and nationalities.index(nationality) != house_index:
                return True
        for nationality in ["Brit", "Swede"]:
            if not any(drink in smokes_adj.get(nationality) for drink in smokes_adj.get(nationality)) or not any(pet in pets for pet in smokes_adj.get(nationality)):
                solution[house_index][nationality] = nationality
                return backtrack(house_index + 1)
        return False

    # Solve the puzzle
    if backtrack(0):
        print("The Norwegian's nationality is:", smokes_adj.get("Norwegian").get("nationality"))
    else:
        print("No solution found.")

solve_puzzle()