import pytest
import sys
import os
import io
import contextlib

# Allow imports from the test execution directory
# This assumes the test runner places the generated file in the same directory.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def test_einstein_riddle_solution():
    """
    Tests the output of the LLM-generated solve_puzzle function.
    It imports the function directly and captures its standard output.
    """
    solution_file = "einstein_solution.py"
    expected_answer = "German"

    try:
        # Dynamically import the generated function
        from einstein_solution import solve_puzzle
    except ImportError:
        pytest.fail(f"Could not import 'solve_puzzle' from '{solution_file}'. The file might be missing or contain syntax errors.")

    captured_output = ""
    try:
        # Capture standard output from the function call
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            solve_puzzle()
            captured_output = buf.getvalue().strip()
        
        print(f"Captured output from solve_puzzle(): '{captured_output}'")
        print(f"Expected answer: '{expected_answer}'")
        
        # Check if the expected answer is present in the captured output
        assert expected_answer in captured_output, \
            f"The puzzle solution is incorrect. Expected to find '{expected_answer}', but got '{captured_output}'."

    except Exception as e:
        pytest.fail(f"The 'solve_puzzle' function produced an unexpected error during execution: {e}\nCaptured output was: '{captured_output}'")