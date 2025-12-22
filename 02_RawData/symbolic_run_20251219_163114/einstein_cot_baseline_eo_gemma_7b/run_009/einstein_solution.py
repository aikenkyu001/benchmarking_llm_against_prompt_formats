def solve_puzzle():
    # 1. Identigu la pozicio de ĉiu domo.
    domoj = {
        1: "Norvego",
        2: "Britano",
        3: "Svedo",
        4: "Dano",
        5: "Verda",
    }

    # 2. Skribu la informojn, kiuj povas esti rekte identigitaj.
    limigoj = {
        "Britano": "ruĝa",
        "Svedo": "hundoj",
        "Dano": "teon",
        "Verda": "kafon",
        "Pall Mall": "birdoj",
        "Dunhill": "flava",
        "Lakton": "centra",
    }

    # 3. Konkludu informojn, kiuj povas esti derivitaj nerekte.
    for domo, persona in domoj.items():
        for limi in limigoj.items():
            if limi[1] == domo:
                domoj[domo] = limi[0]

    # 4. Asignu atributojn al ĉiu domo.
    for domo in domoj.values():
        if domo == "Britano":
            # ...
        elif domo == "Svedo":
            # ...
        # ...

    # 5. Identigu la personon, kiu posedas la fiŝon.
    # ...

    # 6. Returni la naciecon de la posedanto de la fiŝon.
    print("German")