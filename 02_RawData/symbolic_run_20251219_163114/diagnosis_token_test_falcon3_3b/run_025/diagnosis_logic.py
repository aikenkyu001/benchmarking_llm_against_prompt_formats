def diagnose(symptoms: list) -> str:
    if set("High Fever Joint Pain Fatigue".split()) <= symptoms:
        return "Suspected Influenza"
    elif set("Fever Cough").split() <= symptoms:
        return "Suspected Cold"
    elif set("Sneezing Runny Nose Itchy Eyes".split()) <= symptoms:
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"