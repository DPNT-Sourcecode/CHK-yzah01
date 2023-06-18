from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_validations(self):
        assert sum_solution.compute(101, 200) is None

