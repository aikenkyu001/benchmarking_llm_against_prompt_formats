You are an expert Python programmer. Your task is to create a Python script that implements a diagnostic logic system based on the rules defined in the following TSV (Tab-Separated Values) data.

**CRITICAL INSTRUCTIONS:**
- Your output MUST be ONLY a single Python code block.
- The Python script MUST contain one function, `diagnose(symptoms: list) -> str`.
- The `diagnose` function must take a list of symptom strings and return the corresponding diagnosis string.
- The logic must exactly match the rules defined in the TSV. Each row represents a rule. The columns `C1` through `C3` are the conditions, and `Result` is the diagnosis.
- An empty cell in a condition column means that condition is not part of the rule.
- The final rule with `*` in the conditions is the default "else" case.
- DO NOT include any explanation or commentary in your response.

**EXAMPLE OUTPUT FORMAT:**
```python
def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    if {'High Fever', 'Joint Pain', 'Fatigue'}.issubset(symptoms_set):
        return "Suspected Influenza"
    elif {'Fever', 'Cough'}.issubset(symptoms_set):
        return "Suspected Cold"
    # ... and so on
    else:
        return "Consult a Specialist"
```

Now, create the Python script based on the rules in the TSV data below.

**RULES (TSV):**
---
C1	C2	C3	Result
High Fever	Joint Pain	Fatigue	Suspected Influenza
Fever	Cough		Suspected Cold
Sneezing	Runny Nose	Itchy Eyes	Suspected Hay Fever
*	*	*	Consult a Specialist
---
