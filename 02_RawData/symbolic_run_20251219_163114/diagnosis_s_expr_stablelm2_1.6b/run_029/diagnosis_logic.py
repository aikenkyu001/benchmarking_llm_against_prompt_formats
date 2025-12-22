def diagnose(symptoms: list) -> str:
    symptoms_1set = set(symptoms)
    
    if {'High Fever', 'Joint Pain', 'Fatigue'}.issubset(symptoms_1set):
        return "Suspected Influenza"
    elif {'Fever', 'Cough'}.issubset(symptoms_1set):
        return "Suspected Cold"
    elif {'Sneezing', 'Runny Nose', 'Itchy Eyes'}.issubset(symptoms_1set):
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"