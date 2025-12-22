def solve_puzzle():
    # Count how many people are in the room.
    num_people = 5

    # Identify which person has an unsatisfactory smoking habit.
    unsatisfactory_smoker = 0
    for i in range(num_people):
        if (i+1) % 2 == 1:  # British person
            continue
        elif (i+1) % 3 == 0:  # Norwegian person
            continue
        else:
            unsatisfactory_smoker = i

    # Find out what type of cigarette each person smokes.
    brit_cig = "Blend"
    nor_cig = "Royal Oatmeal"
    swi_cig = "Gold Label"
    den_cig = "Pall Mall"
    usa_cig = "Blends"

    # Determine the mark made from cigarettes for each person.
    brit_mark = unsatisfactory_smoker % 3
    nor_mark = (unsatisfactory_smoker + 1) % 3
    swi_mark = unsatisfactory_smoker % 3
    den_mark = unsatisfactory_smoker % 3

    # Find out which person takes a bag containing tobacco.
    brit_bag = "Royal Oatmeal"
    nor_bag = "Gold Label"
    swi_bag = "Blends"
    den_bag = "Pall Mall"

    # Determine the glass of water for each person.
    brit_water = "Royal Oatmeal"
    nor_water = "Gold Label"
    swi_water = "Blends"
    den_water = "Pall Mall"

    # Identify which person smokes a pipe.
    pipe_smoker = 0
    for i in range(num_people):
        if (i+1) % 2 == ..
            pipe_smoker = i

    # Identify the person who takes a cat (contains tobacco) and smokes Blend.
    cat_smoker = pipe_smoker + 1
    blend_smoker = nor_cig

    # Find out the Norwegian person who enters the light room.
    light_room = den_cig

    # Print the solution.
    print("The British person is {}.".format(brit_cig))
    print("The Norwegian person is {}.".format(nor_cig))
    print("The Swedish person is {}.".format(swi_cig))
    print("The Danish person is {}.".format(den_cig))
    print("The American person smokes {}.".format(usa_cig))
    print("The Norwegian person enters the first room.")
    print("The person who takes the blue bag smokes {}.".format(blend_smoker))
    print("The person who takes a cat (contains tobacco) smokes {}.".format(cat_smoker))
    print("The person who enters the center room smokes a pipe.")
    print("The Norwegian person enters the light room.")

solve_puzzle()