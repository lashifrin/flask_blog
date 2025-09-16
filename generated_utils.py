FILENAME: calculator

FUNCTION:
def add(a, b):
    """Add two numbers together.

    Parameters
    ----------
    a : int or float
        The first number to add.
    b : int or float
        The second number to add.

    Returns
    -------
    result : int or float
        The sum of the two numbers.

    """
    return a + b

TESTS:
import calculator
from unittest import TestCase

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0.5, 0.8), 1.3)

if __name__ == '__main__':
    unittest.main()