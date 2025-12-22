def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    for rule in rules:
        if all(condition for condition in rule["if"] in symptoms_set):
            return rule["then"]
    return "Consult a Specialist"