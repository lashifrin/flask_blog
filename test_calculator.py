import calculator
from unittest import TestCase

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0.5, 0.8), 1.3)

if __name__ == '__main__':
    unittest.main()
```