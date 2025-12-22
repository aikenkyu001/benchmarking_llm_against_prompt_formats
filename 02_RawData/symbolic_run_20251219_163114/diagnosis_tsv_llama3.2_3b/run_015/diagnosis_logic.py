def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    rules = [
        {'C1': 'High Fever', 'C2': 'Joint Pain', 'C3': 'Fatigue', 'Result': 'Suspected Influenza'},
        {'C1': 'Fever', 'C2': 'Cough', 'C3': '', 'Result': 'Suspected Cold'},
        {'C1': 'Sneezing', 'C2': 'Runny Nose', 'C3': 'Itchy Eyes', 'Result': 'Suspected Hay Fever'},
        {'C1': '', 'C2': '', 'C3': '', 'Result': 'Consult a Specialist'}
    ]
    for rule in rules:
        if all(rule['C1'] not in symptoms_set or rule['C1'] == '' 
              and all(rule['C2'] not in symptoms_set or rule['C2'] == ''
              and all(rule['C3'] not in symptoms_set or rule['C3'] == ''))
            continue
        if set(rule['C1']) & symptoms_set == set(rule['C1']):
            return rule['Result']
    return "Consult a Specialist"