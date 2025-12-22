def solve_puzzle():
    # Define the sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Pall Mall": "Dunhill", "Dunhill": "Blends", "Bluemaster": "Prince"}
    cats = ["Cat"]

    # Define the backtracking function
    def backtrack(house_index, solution):
        if house_index == 2:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality in ["Brit", "Swede"] for nationality in solution[house_index]):
                return False
            # Constraint 2: The Swede lives in house 2.
            if solution[house_index - 1].get("nationality") != "Swede":
                return False
            return True

        for nationality in nationalities:
            if not any(nationality in ["Brit", "Swede"] for _ in pets):
                solution[house_index] = {"nationality": nationality, "pet": ""}
                used_pet = {"nationality": set(), "pet": set()}
                for pet in pets:
                    if pet not in used_pet["nationality"]:
                        used_pet["nationality"].add(nationality)
                        used_pet["pet"].add(pet)

                # Try to fill the current house
                if solve(house_index + ..