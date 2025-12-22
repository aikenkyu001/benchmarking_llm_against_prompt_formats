def solve_puzzle():
    # Domoj kaj iliaj pozicioj
    homes = {1: "red", 2: "blue", 3: "green", 4: "white", 5: "yellow"}
    positions = {1: "leftmost", 2: "second left", 3: "center", 4: "right", 5: "rightmost"}

    # Personoj kaj iliaj atributoj
    people = {"British": (1, "red", "tea", "Russian", "cigarette"),
              "Swede": (2, "blue", "dog", "Swedish", None),
              "Dane": (3, "green", "tea", None, "Pall Mall"),
              "German": (4, "white", None, "German", None),
              "Norwegian": (5, "yellow", "milk", None, None)}

    # Konkludi aliaj informojn
    for home in homes:
        people[f"Person from {homes[home]} house"] = (positions[home], homes[home], None, None, None)

    # Ripeti procezon por kelkaj atributoj
    for person in people.values():
        if person[-1] is not None:
            person += (person[-1],)
        else:
            person += (None,)

    # Konkludi aliaj informojn
    for person in people.values():
        if len(people) == 1:
            break
        for attribute in ["trinkaĵo", "cigaredo", "dorlotbesto"]:
            if getattr(people[list(people.keys())[0]], attribute) is not None:
                for p in people:
                    if getattr(people[p], attribute) == getattr(people[list(people.keys())[0]], attribute):
                        del people[p]
                        break
            elif len(people) == 1:
                break

    # Ripeti procezon por la restojn atributoj
    for person in people.values():
        if person[-2] is not None:
            person += (person[-2],)
        else:
            person += (None,)

    # Konkludi aliaj informojn
    for person in people.values():
        if len(people) == 1:
            break
        for attribute in ["nacieco"]:
            if getattr(people[list(people.keys())[0]], attribute) is not None:
                for p in people:
                    if getattr(people[p], attribute) == getattr(people[list(people.keys())[0]], attribute):
                        del people[p]
                        break
            elif len(people) == 1:
                break

    # Identigi la posedanto de la fiŝo
    for person in people.values():
        if person[-3] is not None and person[-4] is not None:
            return person[0]