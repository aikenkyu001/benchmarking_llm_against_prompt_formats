def solve_puzzle():
    # Domoj kaj iliaj pozicioj
    homes = {1: "red", 2: "blue", 3: "green", 4: "white", 5: "yellow"}
    positions = {1: "leftmost", 2: "second left", 3: "middle", 4: "right", 5: "rightmost"}

    # Personoj kaj iliaj atributoj
    people = {"British": (1, "red", "tea", "Russian", "cat"),
              "Swede": (2, "blue", "none", "Swedish", "dog"),
              "Dane": (3, "green", "tea", "Danish", "hat"),
              "German": (4, "white", "beer", "German", "birds"),
              "Norwegian": (5, "yellow", "coffee", "Norwegian", "horse")}

    # Kombini la informojn pri domoj kaj personoj
    for home in homes:
        people[homes[home]] = positions[home], homes[home]

    # Konkludu aliaj informojn pri personoj
    for person, (position, color) in people.items():
        if position == "middle":
            people[person][3] = "Lakton"
        elif color == "red":
            people[person][4] = "Russian"
        elif color == "blue":
            if position == "second left":
                people[person][2] = "coffee"
            else:
                people[person][5] = "bluemaster"
                people["Norwegian"][4] = "water"
        elif color == "green":
            if position == "middle":
                people[person][2] = "tea"
            else:
                people[person][5] = "Dunhill"
                people["Swede"][1] = "hund"
        elif color == "white":
            if position == "right":
                people[person][4] = "beer"
                people["German"][2] = "Pall Mall"
            else:
                people[person][5] = "Prince"
        elif color == "yellow":
            if position == "rightmost":
                people[person][4] = "coffee"
            else:
                people[person][5] = "Blends"
                people["Swede"][1] = "cat"

    # Identigu la posedanto de la fiŝo
    for person, (_, _, _, nationality) in people.items():
        if person == "Norwegian":
            continue
        if people[person][5] == "Blends":
            people["Norwegian"][3] = people[nationality][3]
    print(people["Norwegian"][3])