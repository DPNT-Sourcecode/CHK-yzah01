from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):

    def test_checkout_with_valid_input(self):
        self.assertTrue(checkout_solution.checkout("AAABCD"), 195)
        self.assertTrue(checkout_solution.checkout("AAAABBB"), 255)
        self.assertTrue(checkout_solution.checkout("A"), 50)
        self.assertTrue(checkout_solution.checkout("B"), 30)
        self.assertTrue(checkout_solution.checkout("ABAB"), 145)

    def test_checkout_with_invalid_input(self):
        self.assertTrue(checkout_solution.checkout("ABCDE"), -1)
        self.assertTrue(checkout_solution.checkout(""), -1)
        self.assertTrue(checkout_solution.checkout(None), -1)




