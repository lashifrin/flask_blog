FILENAME: calculator

FUNCTION:
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a (int): First integer to be added.
        b (int): Second integer to be added.

    Returns:
        int: Sum of the two integers.
    """
    return a + b

TESTS:
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()