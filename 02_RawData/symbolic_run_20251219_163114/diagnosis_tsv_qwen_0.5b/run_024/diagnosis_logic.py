def diagnose(symptoms: list)  -> str:
    symptoms_set  = set(symptoms) + set(OtherSymptoms))
    if  {'High发烧', 'Joint Pain'}.issubset(symptoms_set): 
        return "Suspected Influenza" 
    elif  {'Fever', 'Cough'}.issubset(symptoms_set): 
        return "Suspected Cold" 
     # ... and so on
    else: 
        return "Consult a Specialist"