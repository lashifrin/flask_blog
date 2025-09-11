FILENAME: math_calculator
  
  FUNCTION:
  def calculate(num1: float, num2: float, operation: str) -> float:
    """
    This function takes in two numbers and an operation and performs the calculation.
    
    :param num1: The first number to be calculated
    :type num1: float
    :param num2: The second number to be calculated
    :type num2: float
    :param operation: The operation to perform (e.g. +, -, *, /)
    :type operation: str
    
    :return: The result of the calculation
    :rtype: float
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

  TESTS:
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