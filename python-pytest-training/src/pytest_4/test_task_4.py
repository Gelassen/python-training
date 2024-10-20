# test_calculator.py

import pytest
from src.pytest_4.calculator import add

# Use @pytest.mark.parametrize to test multiple input sets
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),       # 1 + 2 = 3
    (0, 0, 0),       # 0 + 0 = 0
    (-1, -1, -2),    # -1 + (-1) = -2
    (100, 200, 300), # 100 + 200 = 300
    (1.5, 2.5, 4.0)  # 1.5 + 2.5 = 4.0
])
def test_add(a, b, expected):
    assert add(a, b) == expected
