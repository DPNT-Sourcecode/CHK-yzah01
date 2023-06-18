from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):

    def test_checkout_with_valid_input(self):
        self.assertTrue(checkout_solution.checkout("AAA"), )

    def test_checkout_with_invalid_input(self):
        self.assertTrue(checkout_solution.checkout(), -1)

