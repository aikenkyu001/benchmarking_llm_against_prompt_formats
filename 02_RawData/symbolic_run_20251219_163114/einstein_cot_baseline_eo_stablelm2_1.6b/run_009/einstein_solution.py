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
    tobacco_bags = {
        "British": [],
        "Swedish": ["blue"],
        "Danish": ["green"],
        "Norwegian": ["light"],
        "American": ["black"]
    }
    for i in range(num_people):
        if tobacco_bags[i] and tobacco_bags[i][0] == "other":
            tobacco_bags[i][0] = "t"

    # Identify the person who smokes Blend.
    blend_smoker = None
    for i in range(num_people):
        if tobacco_bags[i].count("t") > 1:
            blend_smoker = i

    # Identify the person who takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = None
    for i in range(num_people):
        if tobacco_bags[i][0] == "other" or tobacco_bags[cat_smoker][0] == "other":
            cat_smoker = i

    # Identify the Norwegian person who enters the light room.
    light_room = None
    for i in range(num_people):
        if tobacco_bags[i].count("light") > ..
            light_room = i

    # Print the result.
  print("The Norwegian person who enters the light room is:", light_room)

solve_puzzle()