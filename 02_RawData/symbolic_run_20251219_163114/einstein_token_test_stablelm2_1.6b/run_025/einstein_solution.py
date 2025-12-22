def solve_puzzle():
    # Define sets for nationalities, drinks, pets, smokes, and colors
    nationalities = ["Brit", "Swede"]
    drinks = ["Tea", "Coffee"]
    pets = ["Dog", "Bird"]
    smokes = ["Pall Mall", "Dunhill"]
    colors = ["Red", "Green", "White", "Yellow", "Blue"]
    
    # Define the house numbers and constraints
    house_numbers = [1, 2, 3, 4, 5]
    constraints = [
        {"nationality": "Brit", "drink": "Tea"},
        {"nationality": "Swede", "pet": pets[0]},
        {"nationality": "Dane", "drink": drinks[0]},
        {"color": "Green", "is_left_of": ["White"]},
        {"color": "Yellow", "is_neighbour_of": ["Red"]}
    ]
    
    # Define the query
  # "Who keeps a Bird as a pet?"
    query = "Based on the constraints, determine the nationality of the person who smokes {}."

    # Function to solve the puzzle using backtracking
    def backtrack(house_index):
        # Base case: if we have filled all houses, check if the solution is valid
        if house_index == 5:
            # Constraint 1: The Brit drinks Tea.
            if not any(nationality in ["Brit", "Swede"] for _ in nationalities) or \
                not any(drink in ["Tea", "Coffee"] for drink in drinks) or \
                not any(pet in pets for pet in [smokes[i] for i in range(len(smokes))]) or \
                not any(color in colors for color in ["Red", "Green", "White", "Yellow", "Blue"]) or \
                not any(house_number in house_numbers for _ in range(5) if house_number != house_index):
                print("Solution found!")
                return

        # Recursive step: Try to fill the current house
        for pet in pets:
            if pet not in used["pet"]:
                solution[house_index]["pet"] = pet
                used["pet"].add(pet)
                
                for drink in drinks:
                    if drink not in used["drink"]:
                        solution[house_index + 1]["drink"] = drink
                        used["drink"].add(drink)
                        
                # Move to the next house
                if solve(house_index + 1):
                    return

        # Backtrack
        used["pet"].remove(pet)

    # Solve the puzzle
    for i in range(len(constraints)):
        if backtrack(i):
            print("Solution found!")
            return
    
    # Print the answer to the query
    print(query.format(smokes[0]))