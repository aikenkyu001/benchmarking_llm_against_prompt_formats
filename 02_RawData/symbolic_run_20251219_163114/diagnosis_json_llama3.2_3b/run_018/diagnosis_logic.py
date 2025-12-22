def diagnose(symptoms: list) -> str:
    rules = [
        {"if": ["High Fever", "Joint Pain", "Fatigue"], "then": "Suspected Influenza"},
        {"if": ["Fever", "Cough"], "then": "Suspected Cold"},
        {"if": ["Sneezing", "Runny Nose", "Itchy Eyes"], "then": "Suspected Hay Fever"}
    ]
    for rule in rules:
        if set(rule["if"]).issubset(set(symptoms)):
            return rule.get("then", "Consult a Specialist")
    return "Consult a Specialist"