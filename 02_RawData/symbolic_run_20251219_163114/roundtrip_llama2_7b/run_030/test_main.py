python
import numpy as np
from main import generate_fibonacci as _generate_fibonacci

def test_generate_fibonacci() -> None:
    """Test the `generate_fibonacci` function."""
    for count in [10]:
        result = _generate_fibonacci(count)
        assert np.all(result == np.take_along(np.arange(count), count)), "Result does not match expected sequence"