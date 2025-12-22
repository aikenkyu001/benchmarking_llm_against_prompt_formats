def diagnose(symptoms: list) -> str:
    # Check if any condition is not present in the symptoms list
    for condition in ['High Fever', 'Joint Pain', 'Fatigue']]:
        if not symptom_list[condition]]:
            return f"Condition {condition} is not present in the symptoms list."
    # If all conditions are present in the symptoms list, return the diagnosis string "Consult a Specialist"
    return "Consult a Specialist"