def solve_puzzle():
    # Count how many people are in the first room (from 1 to 5).
    num_people_in_room = 5

    # Write down all the information that can be uniquely identified from each person.
    unique_info_per_person = {
        "British": {"room": "dark", "person": "the British"},
        "Swedish": {"room": "dark", "person: "the Swedish"},
        "Danish": {"room": "tea", "person": "the Danish"},
        "Red": {"room": "red", "person": "the person who enters the red room"},
        "German": {"room": "pipe", "person": "the German person"},
        "Norwegian": {"room": "first room", "person": "the Norwegian person"},
        "Blends": {"room": "bag with tobacco", "person": "the person who smokes Blends"},
    }

    # Combine all the information obtained from the people in the same room.
    combined_info = {}
    for person, info_dict in unique_info_per_person.items():
        if num_people_in_room <= len(info_dict):
            combined_info[info_dict["room"]] = f"{person} {info_dict['person']}"

    # Identify the person who takes the bag of tobacco and answer the final demand.
    tobacco_bag_taken_by_Norwegian = None
    for info in combined_info.values():
        if "Norwegian" in info:
            tobacco_bag_taken_by_Norwegian = info

    # Print the solution to the final demand.
    print("Tobacco bag taken by Norwegian:", tobacco_bag_taken_by_Norwegian)

# Call the function to solve the puzzle.
solve_puzzle()