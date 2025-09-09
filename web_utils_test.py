import unittest
from flask import Flask

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
    
    def test_addition(self):
        result = calculator(2, 3, '+')
        self.assertEqual(result, 5)
    
    def test_subtraction(self):
        result = calculator(8, 4, '-')
        self.assertEqual(result, 4)
    
    def test_multiplication(self):
        result = calculator(2, 6, '*')
        self.assertEqual(result, 12)
    
    def test_division(self):
        result = calculator(8, 4, '/')
        self.assertAlmostEqual(result, 2)
    
    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator(2, 3, '^')
    
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculator(5, 0, '/')
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
```