import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

    @staticmethod
    def greet():
        print("Hello!")

# Example usage
Calculator.greet()
calc = Calculator(16)
print(calc.square())
