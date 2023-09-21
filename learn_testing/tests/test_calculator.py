# test_calculator.py

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = multiply(2, 7)
        self.assertEqual(result, 14)

    def test_divide(self):
        result = divide(8, 2)
        self.assertEqual(result, 4)

        # Test division by zero
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
