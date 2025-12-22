def diagnose(symptoms: list) -> str:
  """
  Diagnoses a list of symptoms based on the rules defined in the JSON.
  """
  symptoms_set = set(symptoms)
  if 'High Fever' in symptoms_set:
    return "Suspected Influenza"
  elif 'Joint Pain' in symptoms_set:
    return "Suspected Cold"
  elif 'Fatigue' in symptoms_set:
    return "Suspected Hay Fever"
  else:
    return "Consult a Specialist"