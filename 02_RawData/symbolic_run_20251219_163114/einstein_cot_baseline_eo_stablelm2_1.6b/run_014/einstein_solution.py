def solve_puzzle():
    # Uncover the position of each object
    objects = [("Briton", "dark room"), ("Swede", "first room"), ("Dane", "tea room"), ("green room", "coffee room"), ("Norwegian", "center room"), ("Blends", "blue room"), ("Prince", "blue room")]

    # Combine the information from all the literals into one single list or tuple
  combine_objects = []
    
    for obj in objects:
        if len(obj) > 1:  # If there are more than two elements, combine them
            combine_obj = [obj[0]]
            for i in range(1, len(obj)):
                combine_obj.append(combine_obj[-1] + ", " + obj[i])
            combine_objects.append(combine_obj)
        else:
            combine_objects.append(obj)

    # Remove any duplicates from the combined list or tuple
    unique_combo = list(set(combine_objects))

    # Identify the person who owns the blue room and respond with their lighting problem
    if len(unique_combo) == 1:  # If there is only one object left, it's the owner
        print("German")
    else:
        print(unique_combo[0][2])

solve_puzzle()