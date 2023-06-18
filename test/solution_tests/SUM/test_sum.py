from solutions.SUM import sum_solution
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_validations(self):
        with self.assertRaises(ValueError) as ex:
            sum_solution.compute(101, 200)
        self.assertTrue(ex.exception, "Input numbers should be between 0 and 100")


