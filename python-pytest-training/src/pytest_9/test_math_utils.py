# test_math_utils.py
import pytest
from pytest_9.math_utils import divide

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)