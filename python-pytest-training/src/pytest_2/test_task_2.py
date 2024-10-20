# test_calculator.py

import pytest
from src.pytest_2.calculator import divide

def test_divide_zero():
    # Using pytest.raises to check for ZeroDivisionError
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_non_zero():
    # This should not raise any exceptions
    result = divide(10, 2)
    assert result == 5
