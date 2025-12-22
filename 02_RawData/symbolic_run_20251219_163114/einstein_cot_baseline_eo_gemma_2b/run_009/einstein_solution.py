def solve_puzzle():
    # Unue la pozicioni de la 5 kloroj.
    color_positions = [4, 5, 2, 1, 3]

    # Skribamo la informojn, kiuj povas esti rekte identigitaj el ĉiu limigo.
    print("La persono loĝanta en la ruĝa domo tenas hundojn kiel dorlotbestojn.")

    # Konkludu informojn, kiuj povas esti derivitaj nerekte per kombinado de la limigoj.
    print("La persono loĝanta en la centra domo trinkas lakton.")

    # Ripetu ĉi tiun procezon ĝis ĉiuj atributoj.
    person_attributes = ["koloro", "nacieco", "trinkaĵo", "cigaredo", "dorlotbesto"]
    for i, color in enumerate(color_positions):
        person_attributes[i] = "fuma" if i == color else "manej"

    # Identigu la personon, kiu posedas la fiŝon.
    person_name = "Germano"

    # Printu la fina demando.
    print(f"Kiu posedas la {person_name}?")