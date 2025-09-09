import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_calculator_int(self):
        self.assertEqual(calculator(3, 5), 8)

    def test_calculator_float(self):
        self.assertAlmostEqual(calculator(3.5, 5.1), 8.6)

if __name__ == '__main__':
    unittest.main()