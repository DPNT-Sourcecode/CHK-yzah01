from solutions.HLO import hello_solution
import unittest

class TestSum(unittest.TestCase):

    def test_hello_with_valid_name(self):
        self.assertTrue(hello_solution.hello("Joe"), "Hello, Joe!")

    def test_hello_with_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            hello_solution.hello(123)
        self.assertTrue(ex.exception, "name should be of type str")

