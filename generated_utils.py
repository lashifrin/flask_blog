FILENAME: calculator.py

FUNCTION:
def calculate(num1, num2, operation):
    """
    Calculate the result of two numbers based on a given operation.

    :param num1: The first number (float or int)
    :param num2: The second number (float or int)
    :param operation: The operation to perform (str)
    :return: The result of the calculation (float or int)
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Invalid input: num1 and num2 must be numerical values.")
    if not isinstance(operation, str):
        raise ValueError("Invalid input: operation must be a string.")
    if operation.lower() == "add":
        result = num1 + num2
    elif operation.lower() == "subtract":
        result = num1 - num2
    elif operation.lower() == "multiply":
        result = num1 * num2
    elif operation.lower() == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError(f"Invalid operation: {operation}")
    return result

TESTS:
import unittest
from calculator import calculate

class CalculateTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(1, 2, "add"), 3)

    def test_subtract(self):
        self.assertEqual(calculate(5, 3, "subtract"), 2)

    def test_multiply(self):
        self.assertEqual(calculate(10, 2, "multiply"), 20)

    def test_divide(self):
        self.assertEqual(calculate(10, 5, "divide"), 2)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate("a", 2, "add")

if __name__ == '__main__':
    unittest.main()