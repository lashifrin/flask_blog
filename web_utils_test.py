import unittest

class TestCalculator(unittest.TestCase):
    def test_simple_sum(self):
        self.assertEqual(create_simple(3, 5), 8)

if __name__ == '__main__':
    unittest.main()
```