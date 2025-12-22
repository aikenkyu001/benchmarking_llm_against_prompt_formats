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
        "British": "red",
        "Swedish": "blue",
        "Danish": "green",
        "Norwegian": "light",
        "American": "black"
    }
    for i in range(num_people):
        if cigarettes[cigars[i]] != "white":
            cigarettes[cigars[i]] = "other"

    # Determine the mark made from cigarettes for each person.
    marks = {
        "British": "red",
        "Swedish": "blue",
        "Danish": "green",
        "Norwegian": "light",
        "American": "black"
    }
    for i in range(num_people):
        if marks[marks[i]] != cigarettes[cigars[i]]:
            marks[marks[i]] = "other"

    # Find out which person takes a bag containing tobacco.
    tobacco_bag = {
        "British": [],
        "Swedish": ["blonde", "brown"],
        "Danish": ["gray", "white"],
        "Norwegian": ["light", "dark"],
        "American": ["black"]
    }
    for i in range(num_people):
        if tobacco_bag[i] == "other":
            tobacco_bag[i] = None

    # Identify the person who smokes Blend.
    blend_smoker = next((person for person, _ in tobacco_bag.items() if "Blend" in person), None)

    # Find out which person takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = next(
        (person for person, _ in tobacco_bag.items() if "cat" in person),
        None
    )

    # Finally, identify the Norwegian person who enters the light room.
    light_room_norwegian = next((room for room in ["dark", "light"] if "Norwegian" in room), None)

    # Print the result.
  print("The Norwegian person who enters the light room is:", light_room_norwegian)