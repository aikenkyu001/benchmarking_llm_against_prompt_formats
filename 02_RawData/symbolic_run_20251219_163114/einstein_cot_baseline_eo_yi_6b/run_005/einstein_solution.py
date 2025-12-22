def solve_puzzle():
    # Step 1: Identify the position of each room (from 1-a to 5-a)
    positions = {
        'unua': 'German',
        'blua': 'Norvego',
        'centra': 'Blends',
        'blanka': 'Dano',
        'ruĝa': 'Brito'
    }

    # Step 2: Write down the information that can be directly identified from the clues (e.g., the Norvego loĝas en la unua domo)
    clues = {
        '1-a': 'German',
        '2-a': 'Norvego',
        '3-a': 'Blends',
        '4-a': 'Dano',
        '5-a': 'Brito'
    }

    # Step 3: Derive information by combining the clues.
    # Since all people are unique and each person is associated with a room based on clue 1-a to 5-a,
    # we can conclude that the person who posed the fur coat must be in the position of the fur coat's owner.
    posed_fur = positions[clues['4-a']]  # The 4th clue tells us the Dano is in a blue room, so the fur coat must belong to the Brito.

    # Step 4: Identify the person who posed the fur coat and print their nationality.
    print(posed_fur)