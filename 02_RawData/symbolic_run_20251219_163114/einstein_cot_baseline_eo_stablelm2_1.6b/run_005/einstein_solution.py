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
        "Norwegian": "white",
        "American": "black"
    }
    for i in range(num_people):
        if cigarettes[cigars[i]] != "black":
            break

    # Determine the mark made from cigarettes for each person.
    marks = {
        "British": "brown",
        "Swedish": "blue",
        "Danish": "red",
        "Norwegian": "white",
        "American": "black"
    }
    for i in range(num_people):
        if marks[marks[i]] != cigarettes[cigars[i]]:
            break

    # Find out which person takes a bag containing tobacco.
    tobacco_bag = {
        "British": [],
        "Swedish": [],
        "Danish": [],
        "Norwegian": ["light", "dark"],
        "American": []
    }
    for i in range(num_people):
        if tobacco_bag[cigars[i]].count("t") > 1:
            tobacco_bag[cigars[i]].remove("t")
            break

    # Identify the person who smokes Blend.
    blend_smoker = [person for person, _ in tobacco_bag.items() if "Blend" in tobacco_bag[persons[persons.index(x)]]][0]

    # Identify the person who takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = [person for person, _ in tobacco_bag[blend_smoker].items() if "cat" in tobacco_bag[person]][0]

    # Finally, identify the Norwegian person who enters the light room.
    light_room_person = [persons[i] for i in range(num_people) if "Norwegian" in [room[i] for room in ["dark", "light"]]][0]

    # Print the result.
    print("Light room")