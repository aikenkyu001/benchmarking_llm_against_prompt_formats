def solve_puzzle():
    # Define sets for nationalities, drinks, pets, smokes, and colors
    nationalities = ["Brit", "Swede"]
    drinks = ["Tea", "Coffee"]
    pets = ["Dog", "Bird"]
    smokes = ["Pall Mall", "Dunhill"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    
    # Define the puzzle
    house_numbers = [1, 2, 3, 4, 5]
    living_in_house = ["Red", "Green", "Yellow", "Blue"]
    drinks_with_attribute = ["nationality", "drink"]
    is_left_of = ["color"]
    drinks_with_pet = ["pet"]
    
    # Define the constraints
    constraint1 = {"nationality": set(), "drink": set()}
    constraint2 = {"nationality": set(), "drink": set(), "living_in_house": set()}
    constraint3 = {"nationality": set(), "drink": set(), "is_left_of": set()}
    
    # Define the query
  #   "Based on the constraints, determine the nationality of the person who smokes Pall Mall as a pet."
    query = {
        "living_in_house": living_in_house,
        "drinks_with_attribute": drinks_with_attribute,
        "smokes": smokes
    }
    
    # Define the solution
    solution = {}
    
    # Define the backtracking function
    def backtrack(house_index, constraint_set):
        if house_index == 5:
            # Constraint 1: The Brit lives in the Red house.
            if not any(constraint_set["nationality"].__contains__(nationality) for nationality in ["Brit", "Swede"]):
                return False
            # Constraint ..
            # Constraint 8: The Norwegian lives in the first house.
            if solution[house_index]["nationality"] != "Norwegian":
                return False
            return True
        
        for nationality in nationalities:
            if not any(constraint_set["nationality"].__contains__(nationality) for _ in range(len(nationalities))):
                constraint_set["nationality"].add(nationality)
                constraint_set["drink"].add(drink)
                constraint_set["living_in_house"].add(living_in_house)
                
                # Try to fill the current house
                if backtrack(house_index + 1, constraint_set):
                    return True
                
                # Backtrack
                constraint_set["nationality"].remove(nationality)
                constraint_set["drink"].remove(drink)
                constraint_set["living_in_house"].remove(living_in_house)
        
        return False
    
    # Try to solve the puzzle
    if backtrack(0, {}):
        # Find the answer to the query "Who drinks Coffee?"
        for house in solution:
            if house.get("drink") == "Coffee":
                print(house.get("nationality"))
                return
    
# Call the function to solve the puzzle
solve_puzzle()