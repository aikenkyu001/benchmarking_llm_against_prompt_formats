def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    rules = [
        {"if": set(["High Fever", "Joint Pain", "Fatigue"]), "then": "Suspected Influenza"},
        {"if": set(["Fever", "Cough"]), "then": "Suspected Cold"},
        {"if": set(["Sneezing", "Runny Nose", "Itchy Eyes"]), "then": "Suspected Hay Fever"}
    ]
    for rule in rules:
        if set(rule["if"]).issubset(symptoms_set):
            return rule["then"]
    return "Consult a Specialist"