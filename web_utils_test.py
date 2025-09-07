import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_calculator_addition(self):
        self.assertEqual(calculator(1, 2), 3)
    
    def test_calculator_subtraction(self):
        self.assertEqual(calculator(-5, 5), -10)
    
    def test_calculator_multiplication(self):
        self.assertEqual(calculator(2, 3), 6)
    
    def test_calculator_division(self):
        self.assertEqual(calculator(10, 5), 2)

if __name__ == '__main__':
    unittest.main()
```