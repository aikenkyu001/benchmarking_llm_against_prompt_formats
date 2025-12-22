You are a formal specification interpreter. Your task is to transpile a script, written in a symbolic S-expression language, into two syntactically correct and executable Python files: `main.py` and `test_main.py`.

The S-expression script defines a formal specification for a program and its corresponding tests. You must deduce the meaning of the symbolic keywords (e.g., λ, ι, ρ) from their structural context and transpile them into their Python equivalents.

### TASK ###

Translate the following S-expression script into two Python files.

(DEFINE_FILE "main.py"
  (λ generate_fibonacci (ι "count")
    (α result (Σ))
    (α a (ν 0))
    (α b (ν 1))
    (ρ _ (τ (κ "count"))
      (Σ+ result (κ "a"))
      (α temp (+ (κ "a") (κ "b")))
      (α a (κ "b"))
      (α b (κ "temp"))
    )
    (Ω result)
  )
)

(DEFINE_FILE "test_main.py"
  (ζ main generate_fibonacci)
  (λ-test test_generate_fibonacci
    (=
      (λ-call generate_fibonacci 10)
      (Σν 0 1 1 2 3 5 8 13 21 34)
    )
  )
)

### CRITICAL OUTPUT RULES ###
**STRICTLY adhere to these output rules:**
- Output ONLY two Python code blocks and nothing else.
- The first block MUST be ONLY `# main.py` on its own line, followed immediately by its code block. DO NOT include any markdown headings like `**main.py**` before the `# main.py` line.
- The second block MUST be ONLY `# test_main.py` on its own line, followed immediately by its code block. DO NOT include any markdown headings like `**test_main.py**` before the `# test_main.py` line.
- Each code block MUST be enclosed in standard ```python fences.
- Use exactly 4 spaces for indentation.
- For `test_main.py`, ensure test functions start with `test_` and take no arguments.
- When importing functions from `main.py` into `test_main.py`, use `from main import <function_name>`.

---
Now, generate the two files.