def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    if {'High Fever', 'Joint Pain', 'Fatigue'} <= symptoms_set:
        return "Suspected Influenza"
    elif {'Fever', 'Cough'} <= symptoms_set:
        return "Suspected Cold"
    elif {'Sneezing', 'Runny Nose', 'Itchy Eyes'} <= symptoms_set:
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"