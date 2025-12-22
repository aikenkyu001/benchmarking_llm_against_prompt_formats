def solve_puzzle():
    # Uncover the position of each object (from 1 to 5).
    objects = [1, 2, 3, 4, 5]
    
    # Write down all the information that can be easily identified from each lemon.
    lemons = ["Norwegian", "Swedish", "Danish", "Green", "Blue"]
    
    # Combine the information obtained from each lemon into one unified list.
    combined_list = [lemons[i] for i in objects]
    
    # Reduce the combined list by combining multiple elements from the lemons in a single step.
    reduced_list = []
    for i in range(len(combined_list)):
        for j in range(i+1, len(combined_list)):
            if combined_list[j] not in combined_list[i]:
                reduced_list.append(combined_list[i])
                combined_list.pop(j)
    
    # Identify the person who owns the box and respond with their key.
    print("Key:", reduced_list[0])

# Call the function to solve the puzzle.
solve_puzzle()