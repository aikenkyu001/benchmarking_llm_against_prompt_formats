def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    if "High Fever" in symptoms_set and "Joint Pain" in symptoms_set and "Fatigue" in symptoms_set:
        return "Suspected Influenza"
    elif "Fever" in symptoms_set and "Cough" in symptoms_set:
        return "Suspected Cold"
    elif "Sneezing" in symptoms_set and "Runny Nose" in symptoms_set and "Itchy Eyes" in symptoms_set:
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"