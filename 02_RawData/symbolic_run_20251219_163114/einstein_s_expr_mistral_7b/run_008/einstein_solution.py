def solve_puzzle():
    def is_a(obj, domain):
        return f"{obj} is a {domain}"

    def has_property(obj, property, value):
        return f"{obj} has {property} {value}"

    def lives_in(person, house):
        return f"{person} lives in {house}"

    def drinks(person, drink):
        return f"{person} drinks {drink}"

    def smokes(person, smoke):
        return f"{person} smokes {smoke}"

    def keeps_pet(person, pet):
        return f"{person} keeps {pet} as a pet"

    def is_left_of(house1, house2):
        return f"{house1} is on the immediate left of {house2}"

    def is_neighbor_of(house1, house2):
        return f"{house1} and {house2} are neighbors"

    def nationality_of(person):
        return f"nationality of {person}"

    constraints = [
        is_a("p", "person"),
        has_property("p", "nationality", "Brit"),
        has_property("p", "lives_in", "Red house"),

        is_a("p", "person"),
        has_property("p", "nationality", "Swede"),
        has_property("p", "keeps_pet", "Dog"),

        is_a("p", "person"),
        has_property("p", "nationality", "Dane"),
        has_property("p", "drinks", "Tea"),

        is_a("h1", "house"),
        has_property("h1", "color", "Green"),
        is_a("h2", "house"),
        has_property("h2", "color", "White"),
        has_property("h1", "is_left_of", "h2"),

        is_a("p", "person"),
        is_a("h", "house"),
        has_property("h", "color", "Green"),
        has_property("h", "lives_in", "p"),
        has_property("p", "drinks", "Coffee"),

        is_a("p", "person"),
        has_property("p", "smokes", "Pall Mall"),
        has_property("p", "keeps_pet", "Bird"),

        is_a("p", "person"),
        has_property("h", "color", "Yellow"),
        has_property("h", "lives_in", "p"),
        has_property("p", "smokes", "Dunhill"),

        is_a("h", "house"),
        has_number(h, 3),
        has_property("h", "lives_in", "p"),
        has_property("p", "drinks", "Milk"),

        is_a("p", "person"),
        has_property("h", "number", 1),
        has_property("h", "lives_in", "p"),
        has_property("p", "nationality", "Norwegian"),

        is_a("p1", "person"),
        smokes("p1", "Blends"),
        is_a("p2", "person"),
        keeps_pet("p2", "Cat"),
        has_property("p1", "lives_in", "h1"),
        has_property("p2", "lives_in", "h2"),
        has_property("h1", "is_neighbor_of", "h2"),

        is_a("p1", "person"),
        keeps_pet("p1", "Horse"),
        is_a("p2", "person"),
        smokes("p2", "Dunhill"),
        has_property("p1", "lives_in", "h1"),
        has_property("p2", "lives_in", "h2"),
        has_property("h1", "is_neighbor_of", "h2"),

        is_a("p", "person"),
        smokes("p", "Bluemaster"),
        has_property("p", "drinks", "Beer"),

        is_a("p", "person"),
        smokes("p", "Prince"),
        has_property("p", "nationality", "German"),

        is_a("p1", "person"),
        has_property("p1", "nationality", "Norwegian"),
        is_a("h2", "house"),
        has_property("h2", "color", "Blue"),
        has_property("p1", "lives_in", "h1"),
        has_property("h1", "is_neighbor_of", "h2"),

        is_a("p1", "person"),
        smokes("p1", "Blends"),
        is_a("p2", "person"),
        drinks("p2", "Water"),
        has_property("p1", "lives_in", "h1"),
        has_property("p2", "lives_in", "h2"),
        has_property("h1", "is_neighbor_of", "h2")
    ]

    def has_number(house, number):
        return f"{house} has number {number}"

    def find_person_with_pet(pets):
        for constraint in constraints:
            if "keeps_pet" in constraint and pets[constraint.split(" ")[-1]] == "Fish":
                return nationality_of(constraint.split(" ")[0])
        return None

    pets = {"Dog", "Bird", "Cat", "Horse", "Fish"}
    answer = find_person_with_pet(pets)
    print(answer)