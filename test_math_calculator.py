import math_calculator
  
  class TestMathCalculator(unittest.TestCase):
      def test_addition(self):
          self.assertEqual(math_calculator.calculate(2, 3, "+"), 5)
      
      def test_subtraction(self):
          self.assertEqual(math_calculator.calculate(7, 3, "-"), 4)
      
      def test_multiplication(self):
          self.assertEqual(math_calculator.calculate(2, 4, "*"), 8)
      
      def test_division(self):
          self.assertEqual(math_calculator.calculate(10, 2, "/"), 5)
      
      def test_invalid_operation(self):
          with self.assertRaises(ValueError):
              math_calculator.calculate(2, 3, "%%")