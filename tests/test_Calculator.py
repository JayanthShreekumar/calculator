from calc.Calculator import addition, subtraction, multiplication, division
import pytest

def test_addition():
    assert(addition(1, 2) == 3)

# def test_addition_fail():
#     assert(addition(1, 2) == 0)

def test_subtraction():
    assert(subtraction(1, 2) == -1)

def test_multiplication():
    assert(multiplication(1, 2) == 2)

def test_division():
    assert(division(1, 2) == 0.5)

def test_div_by_zero():
    assert(division(1, 0) == "Division by Zero")
