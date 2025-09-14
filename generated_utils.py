FILENAME: calculator

FUNCTION:
def add(x, y):
    """Add two numbers together.

    Args:
        x (int or float): The first number to be added.
        y (int or float): The second number to be added.

    Returns:
        int or float: The sum of the two numbers.
    """
    return x + y

TESTS:
from calculator import add
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(-3, -5), -8)
        self.assertRaises(TypeError, add, "hello", 5)
        self.assertRaises(TypeError, add, 5, "hello")

if __name__ == '__main__':
    unittest.main()