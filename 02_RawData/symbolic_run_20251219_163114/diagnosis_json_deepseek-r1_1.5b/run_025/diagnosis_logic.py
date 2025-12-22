def diagnose(symptoms: list) -> str:
    symptom_set = set(symptoms)
    rules = [
        {
            'if': ['High Fever', 'Joint Pain', 'Fatigue'],
            'then': 'Suspected Influenza'
        },
        {
            'if': ['Fever', 'Cough'],
            'then': 'Suspected Cold'
        },
        {
            'if': ['Sneezing', 'Runny Nose', 'Itchy Eyes'],
            'then': 'Suspected Hay Fever'
        }
    ]
    for rule in rules:
        if symptom_set.issubset(rule['if']):
            return rule['then']
    return "Consult a Specialist"