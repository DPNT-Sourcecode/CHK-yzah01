from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):

    def test_checkout_with_valid_input(self):
        self.assertEqual(checkout_solution.checkout("AAABCD"), 195)
        self.assertEqual(checkout_solution.checkout("AAAABBB"), 255)
        self.assertEqual(checkout_solution.checkout("A"), 50)
        self.assertEqual(checkout_solution.checkout("B"), 30)
        self.assertEqual(checkout_solution.checkout("ABAB"), 145)
        self.assertEqual(checkout_solution.checkout(""), 0)

        self.assertEqual(checkout_solution.checkout("AAAAA"), 200)
        self.assertEqual(checkout_solution.checkout("AAA"), 130)
        self.assertEqual(checkout_solution.checkout("AAAAABBAAAA"), 425)

        self.assertEqual(checkout_solution.checkout("EE"), 80)
        self.assertEqual(checkout_solution.checkout("EEEEEB"), 200)
        self.assertEqual(checkout_solution.checkout("EEEEE"), 200)
        self.assertEqual(checkout_solution.checkout("EEB"), 80)
        self.assertEqual(checkout_solution.checkout("EEEB"), 120)
        self.assertEqual(checkout_solution.checkout("EEEEBB"), 160)


    def test_checkout_with_invalid_input(self):
        self.assertEqual(checkout_solution.checkout(None), -1)
        self.assertEqual(checkout_solution.checkout(1234), -1)





