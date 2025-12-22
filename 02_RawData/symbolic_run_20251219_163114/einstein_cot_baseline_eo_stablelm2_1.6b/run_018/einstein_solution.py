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
        if tobacco_bags[i] and tobacco_bags[i][1] == "other" and marks[blend_smoker] != "other":
            blend_smoker = i

    # Find out which person takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = None
    for i in range(num_people):
        if tobacco_bags[i] and tobacco_bags[i][1] == "other" and marks[cat_smoker] != "other":
            cat_smoker = i

    # Finally, identify the Norwegian person who enters the light room.
    light_room = None
    for i in range(num_people):
        if tobacco_bags[i] and tobacco_bags[i][1] == "other" and marks[light_room] != "other":
            light_room = i

    # Print the result.
    print("The person who smokes Blend is:", blend_smoker)
    print("The person who takes a cat (contains tobacco) and smokes Blend is:", cat_smoker)
    print("The Norwegian person who enters the light room is:", light_room)

# Call the function to solve the puzzle.
solve_puzzle()