You are a formal specification interpreter. Your task is to transpile a script, written in a symbolic S-expression language, into a single, syntactically correct, and executable Python script.

The S-expression script defines a formal specification for a diagnostic logic program. You must deduce the meaning of the symbolic keywords (e.g., λ, Δ, ∧) from their structural context and transpile them into their Python equivalents.

### S-EXPRESSION SCRIPT ###

(λ diagnose ( (symptoms (Σ str)) ) str
    (Δ (∧ (∈ "High Fever" symptoms) (∈ "Joint Pain" symptoms) (∈ "Fatigue" symptoms))
      (Ω "Suspected Influenza")
    )
    (εΔ (∧ (∈ "Fever" symptoms) (∈ "Cough" symptoms))
      (Ω "Suspected Cold")
    )
    (εΔ (∧ (∈ "Sneezing" symptoms) (∈ "Runny Nose" symptoms) (∈ "Itchy Eyes" symptoms))
      (Ω "Suspected Hay Fever")
    )
    (ε
      (Ω "Consult a Specialist")
    )
)

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