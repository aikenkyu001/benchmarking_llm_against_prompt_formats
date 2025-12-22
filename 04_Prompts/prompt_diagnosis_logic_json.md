You are an expert Python programmer. Your task is to create a Python script that implements a diagnostic logic system based on the rules defined in the following JSON structure.

**CRITICAL INSTRUCTIONS:**
- Your output MUST be ONLY a single Python code block.
- The Python script MUST contain one function, `diagnose(symptoms: list) -> str`.
- The `diagnose` function must take a list of symptom strings and return the corresponding diagnosis string.
- The logic must exactly match the rules defined in the JSON. The order of rules matters.
- If no rules match, it should return the 'else' diagnosis.
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

Now, create the Python script based on the rules in the JSON file below.

**RULES (JSON):**
---
```json
[
  {
    "if": ["High Fever", "Joint Pain", "Fatigue"],
    "then": "Suspected Influenza"
  },
  {
    "if": ["Fever", "Cough"],
    "then": "Suspected Cold"
  },
  {
    "if": ["Sneezing", "Runny Nose", "Itchy Eyes"],
    "then": "Suspected Hay Fever"
  },
  {
    "else": "Consult a Specialist"
  }
]
```
---
