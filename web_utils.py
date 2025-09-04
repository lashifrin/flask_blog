FUNCTION:
def calculate(x, y):
    """
    Calculate the sum of two numbers.

    Parameters
    ----------
    x : int or float
        The first number to be calculated.
    y : int or float
        The second number to be calculated.

    Returns
    -------
    result : int or float
        The sum of the two numbers.
    """
    return x + y

TESTS:
import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_calculate_two_positive_numbers(self):
        result = calculate(5, 3)
        self.assertEqual(result, 8)
    
    def test_calculate_one_negative_number(self):
        result = calculate(-5, 3)
        self.assertEqual(result, -2)
    
    def test_calculate_two_negative_numbers(self):
        result = calculate(-5, -3)
        self.assertEqual(result, -8)
    
    def test_calculate_zeroes(self):
        result = calculate(0, 0)
        self.assertEqual(result, 0)
    
    def test_calculate_different_types(self):
        with self.assertRaises(TypeError):
            calculate("5", 3)
        
        with self.assertRaises(TypeError):
            calculate(5, "3")

if __name__ == '__main__':
    unittest.main()