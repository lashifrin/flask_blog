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
```