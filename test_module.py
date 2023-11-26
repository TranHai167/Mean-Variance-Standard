import numpy as np
from numpy.testing import assert_almost_equal
import unittest
import mean_var_std as cal


class TestCalculateMean(unittest.TestCase):
    def test_calculate(self):
        actual = cal.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666],
                         [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949],
                                   [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266],
            'max': [[8, 6, 7], [6, 8, 7], 8], 'min': [[1, 4, 0], [2, 0, 1], 0], 'sum': [[11, 15, 9], [10, 12, 13], 35]}
        self.assertEqual(actual['mean'], expected['mean'])
        self.assertEqual(actual['variance'], expected['variance'])
        self.assertEqual(actual['standard deviation'], expected['standard deviation'])
        self.assertEqual(actual['max'], expected['max'])
        self.assertEqual(actual['min'], expected['min'])
        self.assertEqual(actual['sum'], expected['sum'])

    def test_mean_of_empty_array(self):
        with self.assertRaises(ValueError) as context:
            cal.calculate([2, 6, 2, 8, 4, 0, 1, ])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")


if __name__ == '__main__':
    unittest.main()
