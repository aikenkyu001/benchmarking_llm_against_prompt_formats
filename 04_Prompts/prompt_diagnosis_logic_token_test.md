You are a formal specification interpreter. Your task is to transpile a script, written in a custom token-based language, into a single, syntactically correct, and executable Python script.

The script defines a formal specification for a diagnostic logic program. You must deduce the meaning of the keywords (e.g., begin_FUNCTION, begin_IF) from their structural context and transpile them into their Python equivalents.

### TOKEN-BASED SCRIPT ###

begin_FUNCTION diagnose(symptoms: (list str)) -> str
    begin_IF
        begin_AND
            "High Fever" in symptoms
            "Joint Pain" in symptoms
            "Fatigue" in symptoms
        end_AND
        begin_RETURN "Suspected Influenza" end_RETURN
    end_IF
    begin_ELIF
        begin_AND
            "Fever" in symptoms
            "Cough" in symptoms
        end_AND
        begin_RETURN "Suspected Cold" end_RETURN
    end_ELIF
    begin_ELIF
        begin_AND
            "Sneezing" in symptoms
            "Runny Nose" in symptoms
            "Itchy Eyes" in symptoms
        end_AND
        begin_RETURN "Suspected Hay Fever" end_RETURN
    end_ELIF
    begin_ELSE
        begin_RETURN "Consult a Specialist" end_RETURN
    end_ELSE
end_FUNCTION

### CRITICAL OUTPUT RULES ###
**YOU MUST STRICTLY ADHERE TO THESE RULES. THIS IS NOT A REQUEST, IT IS A COMMAND.**
- Your output must be ONLY one Python code block containing the `diagnose` function.
- Do not include the file name (e.g., `# diagnosis_logic.py`) in your output.
- Do not include any other text, explanation, or conversation.
- The function should be complete and self-contained.

**EXAMPLE OUTPUT FORMAT:**
```python
def diagnose(symptoms: list) -> str:
    symptoms_set = set(symptoms)
    if {'High Fever', 'Joint Pain', 'Fatigue'}.issubset(symptoms_set):
        return "Suspected Influenza"
    elif {'Fever', 'Cough'}.issubset(symptoms_set):
        return "Suspected Cold"
    elif {'Sneezing', 'Runny Nose', 'Itchy Eyes'}.issubset(symptoms_set):
        return "Suspected Hay Fever"
    else:
        return "Consult a Specialist"
```

---
Execute the transpilation now.
