# Simple Calculator

class Calculator:

    def __init__(self):
        self.calc_list = ['+', '-', '*', '/']
        
    def substruction(self):
        return self.num1 - self.num2
    
    def sum(self):
        return self.num1 + self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def calculation(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
        self.num1 = float(input("What is the first number? "))
        while True:
            for i in self.calc_list:
                print(i)
            self.operation = input(f"Please select an operation: ")
            self.num2 = float(input("What is the next number? "))
            if self.operation == '+':
                result = Calculator.sum(self)
                print(f"{self.num1} + {self.num2} = {result}")
            elif self.operation == '-':
                result = Calculator.substruction(self)
                print(f"{self.num1} - {self.num2} = {result}")
            elif self.operation == '/':
                result = Calculator.divide(self)
                print(f"{self.num1} / {self.num2} = {result}")
            else:
                result = Calculator.multiply(self)
                print(f"{self.num1} * {self.num2} = {result}")
            
            question = input(f"Type 'y' to continue calculating with {result}, or type 'q' to exit, or type 's' to start new calculator: ")
            if question == 'y':
                self.num1 = result
                continue
            elif question == 's':
                Calculator.calculation(self, num1=0, num2=0)
            else:
                break


if __name__ == "__main__":
    my_calc= Calculator()
    my_calc.calculation()

## VERY simple calculator

# class Calculator:

#     def __init__(self):
#         self.calc_list = ['+', '-', '*', '/']
        
#     def substruction(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         return self.num1 - self.num2
    
#     def sum(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         return self.num1 + self.num2
    
#     def multiply(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         return self.num1 * self.num2

#     def divide(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         return self.num1 / self.num2

# if __name__ == "__main__":
#     my_calc= Calculator()
#     print(my_calc.multiply(2, 3))
