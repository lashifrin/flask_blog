import unittest
from math_calculator import calculate

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3), 5)
    
    def test_subtraction(self):
        self.assertEqual(calculate(10, -5), 5)
    
    def test_multiplication(self):
        self.assertEqual(calculate(4, 2), 8)
    
    def test_division(self):
        self.assertEqual(calculate(16, 4), 4)

if __name__ == '__main__':
    unittest.main()
```