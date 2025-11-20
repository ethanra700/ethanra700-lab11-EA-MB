# https://github.com/ethanra700/lab11-EA-MB.git
# Partner 1: Ethan A
# Partner 2: Miguel B

import unittest
import math
import calculator


class TestCalculator(unittest.TestCase):

    # Partner 1
    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)
        self.assertEqual(calculator.add(-2, 7), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(4, 10), -6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

    # Partner 2
    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 3), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertEqual(calculator.divide(5, 20), 4)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()
