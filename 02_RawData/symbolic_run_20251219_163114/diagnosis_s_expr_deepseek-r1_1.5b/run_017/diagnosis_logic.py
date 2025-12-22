def diagnose(symptoms: list) -> str:
    set1 = {"High Fever"}
    set2 = {"Joint Pain"}
    set3 = {"Fatigue"}
    set4 = {"Fever"}
    set5 = {"Cough"}
    set6 = {"Sneezing"}
    set7 = {"Runny Nose"}
    set8 = {"Itchy Eyes"}

    if set1.issubset(symptoms) and set2.issubset(symptoms) and set3.issubset(symptoms):
        return "Suspected Influenza"
    elif set4.issubset(symptoms) or set5.issubset(symptoms):
        return "Suspected Cold"
    elif set6.issubset(symptoms) or set7.issubset(symptoms) or set8.issubset(symptoms):
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"