def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    rules = [
        {"if": ["High Fever", "Joint Pain", "Fatigue"], "then": "Suspected Influenza"},
        {"if": ["Fever", "Cough"], "then": "Suspected Cold"},
        {"if": ["Sneezing", "Runny Nose", "Itchy Eyes"], "then": "Suspected Hay Fever"},
        {"else": "Consult a Specialist"}
    ]
    for rule in rules:
        if "if" in rule:
            if symptoms_set.issuperset(rule["if"]):
                return rule["then"]
        elif "else" in rule:
            return rule["else"]
    return "Consult a Specialist"