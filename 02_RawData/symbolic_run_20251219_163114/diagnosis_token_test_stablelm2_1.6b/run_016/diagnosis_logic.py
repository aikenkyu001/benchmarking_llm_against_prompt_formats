def diagnose(symptoms: list) -> str:
    # Replace 'High Fever', 'Joint Pain', etc. with actual conditions
    symptoms_set = set(symptoms)
    
    if {'High Fever', 'Joint Pain', 'Fatigue'}.issubset(symptoms_set):
        return "Suspected Influenza"
    elif {'Fever', 'Cough'}.issubset(symptoms_set):
        return "Suspected Cold"
    elif {'Sneezing', 'Runny Nose', 'Itchy Eyes'}.issubset(symptoms_set):
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"