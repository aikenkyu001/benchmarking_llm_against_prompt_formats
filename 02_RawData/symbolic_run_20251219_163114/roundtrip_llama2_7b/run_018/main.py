python
import numpy as np
from typing import Optional

def generate_fibonacci(count: int) -> list[int]:
    """Generate the Fibonacci sequence up to the given count."""
    a, b = 0, 1
    result = []
    for _ in range(count):
        temp = a + b
        a, b = b, temp
        result.append(b)
    return result
---