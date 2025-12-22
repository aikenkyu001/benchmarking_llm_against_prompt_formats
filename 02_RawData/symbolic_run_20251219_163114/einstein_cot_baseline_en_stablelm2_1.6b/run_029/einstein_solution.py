def solve_puzzle():
    # Step 1: Identify the position of each house
    houses = [0, 1, 2, 3, 4]

    # Step 2: Write down the information that can be directly identified from each constraint
    brit_house = houses[0] if houses[0] == 1 else houses[3]
    norwegian_house = houses[1] if houses[1] == 2 else houses[4]
    british_pet = "bird" if houses[5] == 2 else "cat"
    swedish_pet = "dog" if houses[6] == 3 else "horse"

    # Step 3: Infer information that can be derived indirectly by combining the constraints
    green_house_beverage = (houses[0] == 1 and houses[4] == 2) or (houses[0] == 2 and houses[4] == 3)
    green_house_cigar = (houses[0] == 1 and houses[5] == 2) or (houses[0] == 2 and houses[5] == 3)

    # Step 4: Repeat this process until all attributes are assigned to each house
    for i in range(5):
        if green_house_beverage[i] or green_house_cigar[i]:
            continue

        # Assign the remaining information based on the constraints
        british_smoker = (houses[0] == 1 and houses[6] == 4) or (houses[0] == 2 and houses[7] == 5)
        swedish_smoker = (houses[0] == 1 and houses[8] == 9) or (houses[0] == 2 and houses[9] == 10)

        # Assign the pet based on the smokers' pets
        if british_smoker:
            pet = "bird"
        elif swedish_smoker:
            pet = "cat"
        else:
            pet = "horse"

        # Update the house information
        houses[i] = (houses[i] + 1) % 5

    # Step 5: Identify the person who owns the fish and state their nationality
    fish_owner = houses[4]

    # Print the final answer
    print(f"The Norwegian owns the fish. Their nationality is {fish_owner}'.")

# Test the function with an example output
solve_puzzle()