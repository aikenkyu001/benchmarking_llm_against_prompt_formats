def diagnose(symptoms: list) -> str:
    if symptoms:
        symptoms_set = set(symptoms)
        if 'High Fever' in symptoms and 'Joint Pain' in symptoms and 'Fatigue' in symptoms:
            return "Suspected Influenza"
        elif 'Fever' in symptoms and 'Cough' in symptoms:
            return "Suspected Cold"
        elif 'Sneezing' in symptoms and 'Runny Nose' in symptoms and 'Itchy Eyes' in symptoms:
            return "Suspected Hay Fever"
    return "Consult a Specialist"