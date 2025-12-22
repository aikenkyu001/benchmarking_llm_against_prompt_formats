def diagnose(symptoms: list) -> str:
    # Check if any condition is not present in the symptoms list
    for condition in ['High Fever', 'Joint Pain', 'Fatigue']]:
        if not symptom_list.contains(condition):
            return f"Condition {condition} is not present in the symptoms list. Consult a Specialist."
    
    # If all conditions are present in the symptoms list, return the diagnosis string "Suspected Influenza"
    return f"Suspected Influenza."