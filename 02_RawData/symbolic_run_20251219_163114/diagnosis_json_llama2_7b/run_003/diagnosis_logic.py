def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    for rule in rules:
        if rule["if"] <= symptoms_set:
            return rule["then"]
    else:
        return rule["else"]