def diagnose(symptoms: list)  -> str:
    symptoms_set = set(symptoms)
    
    if {'High Fever', 'Joint Pain', 'Fatigue'}.issubset(symptoms_set):
        return "Suspected Influenza"
    elif {'Fever', 'Cough'}.issubset(symptoms_set):
        return "Suspected Cold"
    
    # ... and so on for the remaining conditions
    
    else:
        return "Consult a Specialist"