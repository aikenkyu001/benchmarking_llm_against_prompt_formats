def solve_puzzle():
    # Count how many people are there in the room (5).
    num_people = 5

    # Identify which person has an unsatisfactory smoking habit.
    unsatisfactory_smoker = 0
    for i in range(num_people):
        if "unhappy" in str(i) or "angry" in str(i):
            unsatisfactory_smoker += 1
            break

    # Find out what type of cigarette each person smokes.
    cigarettes = ["C", "B", "A", "S"]
    for i in range(num_people):
        if cigarettes[i] == "B":
            print(f"{i+1} is smoking Blend.")
        elif cigarettes[i] == "A":
            print(f"{i+1} is smoking Blend.")
        elif cigarettes[i] == "S":
            print(f"{i+1} is smoking Smark.")

    # Determine the mark made from cigarettes for each person.
    marks = ["", "", "", "", ""]
    for i in range(num_people):
        if cigarettes[i] == "B":
            marks[marks.index("")] += "B"
        elif cigarettes[i] == "A":
            marks[marks.index("")] += "A"
        elif cigarettes[i] == "S":
            marks[marks.index("")] += "S"

    # Find out which person takes a bag containing tobacco.
    for i in range(num_people):
        if "bag" in str(i) or "tobacco" in str(i):
            print(f"{i+1} is taking a bag containing tobacco.")

    # Identify the person who smokes Blend.
    blend_smoker = 0
    for i in range(num_people):
        if cigarettes[blend_smoker] == "B":
            print(f"{i+1} is smoking Blend.")
            break

    # Identify the person who takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = 0
    for i in range(num_people):
        if "cat" in str(i) or "tobacco" in str(i):
            print(f"{i+..
1. The Norwegian person enters the light room.

2. The solution is found by following the logic and rules provided above.

**Python Solution:**