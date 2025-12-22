def solve_puzzle():
    # Define sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Pall Mall": 1, "Dunhill": 2, "Blends": 3, "Bluemaster": 4, "Prince": 5}

    # Define the function to solve the puzzle
    def backtrack(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 2:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality for nationality in nationalities if nationality != "Brit") or \
                not any(drink for drink in drinks if drink != "Tea" and drink != "Coffee") or \
                not any(smoke for smoke in smokes_adj if smoke != "Pall Mall" and smoke != "Dunhill"):
                return True
            # Constraint 2: The Swede lives in house 2.
            if nationalities.index("Swede") == house_index - 1:
                return True
        # Recursive step: Try to fill the current house (house_index)
        for nationality in nationalities:
            if not any(nationality for nationality in nationalities) or \
                not any(drink for drink in drinks if drink != "Tea" and drink != "Coffee") or \
                not any(smoke for smoke in smokes_adj if smoke != "Pall Mall" and smoke != "Dunhill"):
                solution[house_index]["nationality"] = nationality
                used["nationality"].add(nationality)
                for smoke in smokes_adj:
                    if smoke not in used["smokes"]:
                        solution[house_index + 1]["drink"] = smoke
                        used["smokes"].add(smoke)
                        if solve(house_index + 1):
                            return True
                used["nationality"].remove(nationality)
        return False

    # Solve the puzzle
    if backtrack(0):
        print("The answer to the query is:", nationalities[used["nationality"][-1]])

# Call the function to solve the puzzle
solve_puzzle()