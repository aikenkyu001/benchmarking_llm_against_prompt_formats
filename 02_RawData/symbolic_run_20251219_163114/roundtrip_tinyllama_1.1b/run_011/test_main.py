` on its own line, followed immediately by its code block. DO NOT include any markdown headings like `**test_main.py**` before the `# test_main.py` line.
- Each code block MUST be enclosed in standardpython fences.
- Use exactly 4 spaces for indentation.
- For `test_main.py`, ensure test functions start with `test_` and take no arguments.
- When importing functions from `main.py` into `test_main.py`, use `from main import <function_name>` instead of `import main`. This ensures that the function is only imported once, and not twice for each test function.