import pytest
from dumb_code import add, subtract, multiply, divide

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
        
