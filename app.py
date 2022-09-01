class Calculator:
    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def subtraction(self, x, y):
        return x - y

    def adding(self, x, y):
        return x + y


class ComplicatedCalculator:
    def __init__(self, field=0):
        self.field = field


def adding_static(x, y):
    return x + y