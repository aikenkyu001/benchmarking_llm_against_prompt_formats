from main import generate_fibonacci
import unittest

class TestFibonacci(unittest.TestCase):
    def test_generate_fibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(generate_fibonacci(10), expected)

if __name__ == '__main__':
    unittest.main()
---
The error:
---
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /private/test/benchmarking_llm_against_prompt_formats/02_RawData/symbolic_run_20251219_163114/roundtrip_yi_6b/run_018
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test_main.py _________________________
/private/test/.venv/lib/python3.9/site-packages/_pytest/python.py:498: in importtestmodule
    mod = import_path(
/private/test/.venv/lib/python3.9/site-packages/_pytest/pathlib.py:587: in import_path
    importlib.import_module(module_name)
/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1030: in _gcd_import
    ???
<frozen importlib._bootstrap>:1007: in _find_and_load
    ???
<frozen importlib._bootstrap>:986: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:680: in _load_unlocked
    ???
/private/test/.venv/lib/python3.9/site-packages/_pytest/assertion/rewrite.py:177: in exec_module
    source_stat, co = _rewrite_test(fn, self.config)
/private/test/.venv/lib/python3.9/site-packages/_pytest/assertion/rewrite.py:357: in _rewrite_test
    tree = ast.parse(source, filename=strfn)
/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ast.py:50: in parse
    return compile(source, filename, mode, flags,
E     File "/private/test/benchmarking_llm_against_prompt_formats/02_RawData/symbolic_run_20251219_163114/roundtrip_yi_6b/run_018/test_main.py", line 12
E       Now you can regenerate the Python code blocks following these rules:
E           ^
E   SyntaxError: invalid syntax
=========================== short test summary info ============================
ERROR test_main.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================