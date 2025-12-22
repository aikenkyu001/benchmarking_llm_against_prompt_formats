def solve_puzzle():
    # Define the sets and constraints
    house_numbers = [1, 2, 3, 4, 5]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    smokes = ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]
    pets = ["Dog", "Bird", "Cat", "Horse", "Fish"]
    smokes_adj = {"Pall Mall": "yes", "Dunhill": "yes", "Blends": "yes", "Bluemaster": "yes", "Prince": "yes"}
    pets_adj = {"Dog": "yes", "Bird": "yes", "Cat": "yes", "Horse": "yes", "Fish": "yes"}

    # Define the function to solve the puzzle
    def backtrack(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 5:
            # Constraint 1: The Brit drinks Tea.
            if not any(nat in ["Brit", "Swede"] for nat in [colors[house_index]]):
                return False
            # Constraint 2: The Swede lives in house 2.
            if nationalities[house_index] != "Swede":
                return False
            return True

        # Recursive step: Try to fill the current house (house_index)
        for nat in [nationalities[house_index]]:
            if not any(sm in smokes_adj for sm in smokes):
                solution(house_index)["nationality"] = nat
                used["nationality"].add(nat)

                for drk in drinks:
                    if not any(sm in smokes_adj for sm in ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"]) or \
                       not any(drink in ["Tea", "Coffee"] for drink in [drinks[house_index]]):
                        solution(house_index)["drink"] = drk
                        used["drink"].add(drk)

                        # Move to the next house
                        if solve(house_index + ..
                               "return")
                            return True

                # Backtrack
                used["nationality"].remove(nat)
                used["drink"].remove(drk)

        return False

    # Define the function to find the answer to the query
    def get_pet():
        for pet in pets_adj:
            if pets[pet] == "yes":
                return pet

    # Solve the puzzle
    solution = {}
    for i in range(len(house_numbers)):
        solution[i] = {"nationality": None, "drink": None}
        used["nationality"].add(nationalities[i])
        used["drink"].add(drinks[i])

        if backtrack(i + 1):
            return get_pet()

    # Print the answer to the query
    print("The Norwegian lives in house", solution[0].get("nationality"), "and smokes", solution[0].get("smokes"))

# Call the solve_puzzle function
solve_puzzle()