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
```