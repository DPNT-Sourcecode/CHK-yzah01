from solutions.HLO import hello_solution
import unittest

class TestSum(unittest.TestCase):

    def test_input_below_0(self):
        self.assertTrue(hello_solution.hello("joe"), "Hello, World!")


