def solve_puzzle():
    # Step 1: Determine the location of each house (1-5)
    houses = ["Norwegian", "Swedish", "Danish", "Green", "Yellow"]

    # Step 2: Write down direct information from constraints
    norwegian_house = 1
    swedish_pet = "dog"
    danish_drink = "tea"

    # Step 3: Infer indirect information by combining constraints
    green_house_left_yellow = True
    coffee_drinker_lives_in_green = True
    pipe_smoker_lives_next_to_bird_keeper = True
    milk_drinker_lives_in_middle_house = True

    # Step 4: Assign attributes to each house
    houses[norwegian_house - 1] = {"nationality": "Norwegian", "drink": None, "smoke": None, "pet": None}
    houses[0]["pet"] = swedish_pet

    for i in range(5):
        if green_house_left_yellow and i == 2:
            houses[i] = {"color": "green", "nationality": None, "drink": "coffee", "smoke": None, "pet": None}
        elif milk_drinker_lives_in_middle_house and i == 2:
            houses[i] = {"drink": "milk"}
        elif pipe_smoker_lives_next_to_bird_keeper and i == 3:
            houses[i - 1]["smoke"] = "pipe"
            houses[i] = {"pet": "bird"}

    # Step 5: Determine the fish keeper's nationality
    for house in houses:
        if house["drink"] == "beer" and house["smoke"] == "Bullmaster":
            print("German")