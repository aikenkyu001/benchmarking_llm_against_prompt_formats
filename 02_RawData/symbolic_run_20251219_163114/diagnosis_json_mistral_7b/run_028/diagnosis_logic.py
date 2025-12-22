def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    rules = [{'if': set(rule['if']), 'then': rule['then']} for rule in json.loads(json.dumps(rules))]
    for rule in rules:
        if rule['if'].issubset(symptoms_set):
            return rule['then']
    return "Consult a Specialist"