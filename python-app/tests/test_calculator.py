import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(4, 2) == 2.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(4, 0)
