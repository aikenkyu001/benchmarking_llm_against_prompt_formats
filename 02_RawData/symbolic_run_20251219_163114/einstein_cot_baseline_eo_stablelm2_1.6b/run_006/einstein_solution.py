def solve_puzzle():
    # Count how many people are there in the room (5).
    num_people = 5

    # Identify which person has an unsatisfactory smoking habit.
    unsatisfactory_smoker = 0
    for i in range(num_people):
        if "Norwegian" in [room[i] for room in ["dark", "light"]]:
            unsatisfactory_smoker += 1
            break

    # Find out what type of cigarette each person smokes.
    cigarettes = {
        "British": "brown",
        "Swedish": "blue",
        "Danish": "red",
        "Norwegian": "light",
        "German": "black"
    }
    for i in range(num_people):
        if cigarettes[cigars[i]] != "white":
            cigarettes[cigars[i]] = "another color"

    # Determine the mark made from cigarettes for each person.
    marks = {
        "British": "brown",
        "Swedish": "blue",
        "Danish": "red",
        "Norwegian": "light",
        "German": "black"
    }
    for i in range(num_people):
        if marks[room[i]] != cigarettes[cigars[i]]:
            marks[room[i]] = cigarettes[cigars[i]]

    # Find out which person takes a bag containing tobacco.
    tobacco_bags = {
        "British": [],
        "Swedish": ["blue", "brown"],
        "Danish": ["red"],
        "Norwegian": ["light", "black"],
        "German": ["black"]
    }
    for i in range(num_people):
        if tobacco_bags[room[i]] == "blue":
            tobacco_bags[room[i]].append("tobacco")
            break

    # Identify the person who smokes Blend.
    blend_smoker = None
    for bag, smokers in tobacco_bags.items():
        if "Blend" in smokers:
            blend_smoker = smokers.index("Blend") + 1
            break

    # Find out which person takes a cat (contains tobacco) and smokes Blend.
    cat_smokers = {
        "British": [],
        "Swedish": ["blue", "brown"],
        "Danish": ["red"],
        "Norwegian": ["light", "black"],
        "German": ["black"]
    }
    for i in range(num_people):
        if cat_smokers[room[i]] == smokers:
            cat_smokers[room[i]].remove(smokers)
            break

    # Identify the Norwegian person who enters the light room.
    norwegian_smoker = None
    for smoker, rooms in tobacco_bags.items():
        if "light" in rooms:
            norwegian_smoker = smoker
            break

    # Print the result based on the logic.
    if unsatisfactory_smoker == 0:
        print("German")
    elif num_people - 1 == len(blend_smoker) + len(norwegian_smoker):
        print("Norwegian")
    else:
        print(f"{blend_smoker} and {norwegian_smoker}")

solve_puzzle()