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
            # Constraint 1: The Brit lives in the Red house.
            if not any(nationality for nationality in nationalities if nationality != pet) or \
                not any(drink for drink in drinks_adj if drink != "Tea" and drink != "Coffee") or \
                not any(smoke for smoke in smokes_adj if smoke != "Pall Mall" and smoke != "Dunhill"):
                return True
            # Constraint 2: The Swede keeps Dogs as pets.
            if pet == "Dog":
                return True
            # Constraint 3: The Dane drinks Tea.
            if tea not in drinks_adj:
                return True
            # Constraint 4: The Green house is on the left of the White house.
            if green_house_index not in house_numbers:
                return True
            # Constraint 5: The Green house' owner drinks Coffee.
            if coffee not in drinks_adj:
                return True
            # Constraint 6: The person who smokes Pall Mall rears Birds.
            if pall_mall_not_in_smokes_adj:
                return True
            # Constraint 7: The owner of the Yellow house smokes Dunhill.
            if yellow_house_index not in house_numbers:
                return True
            # Constraint 8: The man living in the center house drinks Milk.
            if milk_not_in_drinks_adj:
                return True
            # Constraint 9: The Norwegian lives in the first house.
            if norwegian_not_in_houses_adj:
                return True

        # If none of the constraints are met, backtrack to try a different pet and house index
        for i in range(len(nationalities)):
            if nationalities[i] not in used_nationalities:  # Check if the nationality is already used
                used_nationalities.add(nationalities[i])
                used_smokes_adj[nationality].append(smoke)
                used_drinks_adj[drink].append(tea)
                used_houses_adj.append(house_index + 1)
                if solve(house_index + 1, i):
                    return True
                used_nationalities.remove(nationalities[i])
                used_smokes_adj[nationality].remove(smoke)
                used_drinks_adj[drink].remove(tea)
                used_houses_adj.remove(house_index + 1)

        return False

    # Start the backtracking process with house index 0 and pet "Dog"
    if solve(0, "Dog"):
        print("The Norwegian's nationality is:", nationalities[pet - 1])
        return
    else:
        print("No solution found.")

# Define the sets for each category
sets = {
    "house_numbers": [i for i in range(len(house_numbers))],
    "nationalities": ["".join(nationality) for nationality in nationalities],
    "drinks": ["".join(drink) for drink in drinks],
    "smokes": ["".join(smoke) for smoke in smokes],
    "pets": ["".join(pet) for pet in pets],
    "smokes_adj": {"Red": [], "Green": [], "Blue": []},
    "drinks_adj": {"Tea": [], "Coffee": [], "Milk": [], "Beer": [], "Water": []}
}

# Define the puzzle
puzzle = {
    "begin_DEFINE_SETS": sets,
    "begin_DEFINE_CONSTRAINTS": [
        "The Brit drinks Tea.",
        "The Swede lives in house 2.",
        "The Brit lives in the Red house."
    ],
    "begin_QUERY": ["Who drinks Coffee?"]
}

# Solve the puzzle
solve_puzzle()