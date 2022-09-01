import pytest
from app import Calculator

calc = Calculator()


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self.calc, 2, 2) == 4

    def test_multiplying(self):
        assert self.calc.multiply(self.calc, -2, 2) == -4

    def test_dividing(self):
        assert self.calc.division(self.calc, -2, -2) == 1

    def test_substricting(self):
        assert self.calc.subtraction(self.calc, -2, 0) == -2

    def test_adding5(self):
        assert self.calc.adding(self.calc, 1.5, 1.5) == 3