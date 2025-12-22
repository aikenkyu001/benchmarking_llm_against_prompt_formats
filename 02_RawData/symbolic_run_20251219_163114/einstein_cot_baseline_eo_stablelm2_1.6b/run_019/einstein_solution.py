def solve_puzzle():
    # Count how many people are there in the room (5).
    num_people = 5

    # Identify which person has an unsatisfactory smoking habit.
    unsatisfactory_smoker = 0
    for i in range(num_people):
        if "Norwegian" in ["British", "Swedish", "Danish", "Red"] and i != unsatisfactory_smoker:
            unsatisfactory_smoker += 1

    # Find out what type of cigarette each person smokes.
    cigarettes = {"Pipe": 0, "Cig": 0, "Tea": 0}
    for i in range(num_people):
        if i == unsatisfactory_smoker:
            continue
        if "Pipe" in cigarettes.keys():
            cigarettes["Pipe"] += 1
        elif "Cig" in cigarettes.keys():
            cigarettes["Cig"] += ..
        elif "Tea" in cigarettes.keys():
            cigarettes["Tea"] += 1

    # Determine the mark made from cigarettes for each person.
    marks = {"Pipe": 0, "Cig": 0, "Tea": 0}
    for i in range(num_people):
        if i == unsatisfactory_smoker:
            continue
        if "Pipe" in marks.keys():
            marks["Pipe"] += cigarettes["Pipe"]
        elif "Cig" in marks.keys():
            marks["Cig"] += cigarettes["Cig"]
        elif "Tea" in marks.keys():
            marks["Tea"] += cigarettes["Tea"]

    # Find out which person takes a bag containing tobacco.
    tobacco_bag = 0
    for i in range(num_people):
        if i == unsatisfactory_smoker:
            continue
        if "Norwegian" in ["British", "Swedish", "Danish", "Red"]:
            tobacco_bag += 1

    # Identify the person who smokes Blend.
    blend_smoker = 0
    for i in range(num_people):
        if i == unsatisfactory_smoker:
            continue
        if "Blend" in cigarettes.keys():
            blend_smoker += 1

    # Find out which person takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = 0
    for i in range(num_people):
        if i == unsatisfactory_smoker:
            continue
        if "Cat" in marks.keys():
            cat_smoker += 1

    # Finally, find the Norwegian person in the light room.
    light_room_person = 0
    for i in range(num_people):
        if i != unsatisfactory_smoker and i == light_room_person:
            continue
        if "Norwegian" in ["British", "Swedish", "Danish", "Red"]:
            light_room_person += 1

    # Print the solution.
    print("Person {} smokes a {} cigarette.".format(unsatisfactory_smoker, cigarettes["Pipe"]))
    print("Person {} smokes a {} cigarette.".format(blend_smoker, cigarettes["Cig"]))
    print("Person {} smokes a {} cigarette.".format(cat_smoker, cigarettes["Tea"]))
    print("Person {} takes a {} tobacco bag.".format(tobacco_bag, tobacco_bag))
    print("Person {} smokes Blend.".format(blend_smoker))
    print("Person {} takes a cat (contains tobacco) and smokes Blend.".format(cat_smoker))
    print("Person {} enters the light room.".format(light_room_person))

solve_puzzle()