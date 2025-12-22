def solve_puzzle():
    # Define sets for nationalities, drinks, pets, smokes, and colors
    nationalities = ["Brit", "Swede"]
    drinks = ["Tea", "Coffee"]
    pets = ["Dog", "Bird"]
    smokes = ["Pall Mall", "Dunhill"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    
    # Define the puzzle
    house_numbers = [1, 2, 3, 4, 5]
    living_in_house = ["Red"]
    drinks_with_attribute = ["nationality"]
    is_left_of = ["color"]
    drinks_with_pet = ["pet"]
    keeps_pet = ["nationality"]
    
    # Define the constraints
    constraint_1 = {"nationality": set(), "drink": set()}
    constraint_2 = {"nationality": set(), "drink": set(), "pet": set()}
    constraint_3 = {"nationality": set(), "drink": set(), "pet": set(), "smokes": set()}
    
    # Define the query
  #   "Based on the constraints, determine the nationality of the person who keeps Fish as a pet."
    query = "Based on the constraints, determine the nationality of the person who keeps {pet} as a pet."

    # Define the solution
    solution = {}
    
    # Define the backtracking function
    def backtrack(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 5:
            # Constraint 1: The Brit drinks Tea.
            if not any(nat in living_in_house for nat in nationalities) or \
                not any(drink in drinks_with_attribute for drink in drinks) or \
                not any(pet in pets for pet in pets) or \
                not any(smoke in smokes for smoke in smokes):
                return True
            # Constraint ..
        else:
            # Recursive step: Try to fill the current house (house_index)
            for nat in nationalities:
                if nat not in constraint_1["nationality"]:
                    solution[house_index] = {"nationality": nat, "pet": pet}
                    constraint_1["nationality"].add(nat)
                    constraint_2["nationality"].add(nat)
                    constraint_3["nationality"].add(nat)
                    if solve(house_index + 1):
                        return True
                    constraint_1["nationality"].remove(nat)
            # Backtrack
            constraint_1["nationality"].remove(nat)

        return False

    # Solve the puzzle
    if backtrack(0):
        # Find the answer to the query "Who drinks Coffee?"
        for house in solution:
            if house.get("drink") == "Coffee":
                print(house.get("nationality"))
                return
    
# Call the function to solve the puzzle
solve_puzzle()