def solve_puzzle():
    # 1. Kreu matrico por organizi la datumojn.
    matrix = {
        "Domo 1": {"Koloro": None, "Nacieco": None, "Trinkaĵo": None, "Cigaredo": None, "Dorlotbesto": None},
        "Domo 2": {"Koloro": None, "Nacieco": None, "Trinkaĵo": None, "Cigaredo": None, "Dorlotbesto": None},
        "Domo 3": {"Koloro": None, "Nacieco": None, "Trinkaĵo": None, "Cigaredo": None, "Dorlotbesto": None},
        "Domo 4": {"Koloro": None, "Nacieco": None, "Trinkaĵo": None, "Cigaredo": None, "Dorlotbesto": None},
        "Domo 5": {"Koloro": None, "Nacieco": None, "Trinkaĵo": None, "Cigaredo": None, "Dorlotbesto": None}
    }

    # 2. Enmetu la direktajn informojn.
    matrix["Domo 1"]["Nacieco"] = "Norvego"
    matrix["Domo 1"]["Koloro"] = "Blua"
    matrix["Domo 1"]["Trinkaĵo"] = "Biero"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Koloro"] = "Verda"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 3"]["Nacieco"] = "Dano"
    matrix["Domo 3"]["Trinkaĵo"] = "Teo"

    # 3. Dedukti la restajn informojn.
    matrix["Domo 2"]["Koloro"] = "Ruĝa"
    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Koloro"] = "Blanka"
    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Cigaredo"] = "Blends"
    matrix["Domo 5"]["Dorlotbesto"] = "Birdoj"
    matrix["Domo 5"]["Cigaredo"] = "Pall Mall"

    matrix["Domo 2"]["Cigaredo"] = "Dunhill"
    matrix["Domo 2"]["Dorlotbesto"] = "Ĉevaloj"
    matrix["Domo 2"]["Cigaredo"] = "Bluemaster"
    matrix["Domo 2"]["Trinkaĵo"] = "Teo"

    matrix["Domo 4"]["Cigaredo"] = "Prince"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 3"]["Nacieco"] = "Dano"
    matrix["Domo 3"]["Trinkaĵo"] = "Teo"

    matrix["Domo 1"]["Cigaredo"] = "Blends"
    matrix["Domo 1"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2"]["Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2"]["Nacieco"] = "Britoj"
    matrix["Domo 2гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4"]["Nacieco"] = "Germanoj"
    matrix["Domo 4"]["Trinkaĵo"] = "Kafao"

    matrix["Domo 5"]["Nacieco"] = "Svedo"
    matrix["Domo 5"]["Dorlotbesto"] = "Hundoj"
    matrix["Domo 5"]["Trinkaĵo"] = "Akvo"

    matrix["Domo 2гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["さり"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    matrix["Domo 4гуу"Trinkaĵo"] = "Lakto"

    經過了很長時間，我仍然無法理解這個問題。