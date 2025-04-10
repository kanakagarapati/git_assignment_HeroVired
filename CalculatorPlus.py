import math
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    num1 = 5
    num2 = 3
    nub2 = 25
    print(f"{num1} + {num2} = {calc.add(num1, num2)}")
    print(f"{num1} - {num2} = {calc.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calc.divide(num1, num2)}")

