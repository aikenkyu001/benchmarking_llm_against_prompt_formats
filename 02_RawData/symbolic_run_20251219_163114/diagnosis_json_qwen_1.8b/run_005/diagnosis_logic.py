def diagnose(symptoms: list) -> str:
    if 'High Fever' in symptoms or 'Joint Pain' in symptoms or 'Fatigue' in symptoms:
        return "Suspected Influenza"
    elif 'Fever' in symptoms or 'Cough' in symptoms or 'Itchy Eyes' in symptoms:
        return "Suspected Cold"
     # ... and so on
    else:  # No rules match the given symptoms
        return "Consult a Specialist"  # If no rule matches, return the diagnosis string