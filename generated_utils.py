FILENAME: calculator.py

FUNCTION:
def add(a, b):
    """
    Add two numbers

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of the two numbers
    """
    return a + b

def subtract(a, b):
    """
    Subtract two numbers

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Difference of the two numbers
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Product of the two numbers
    """
    return a * b

def divide(a, b):
    """
    Divide two numbers

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Quotient of the two numbers
    """
    return a / b

TESTS:
import calculator
from unittest import TestCase

class CalculatorTest(TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_division(self):
        self.assertEqual(calculator.divide(8, 2), 4)