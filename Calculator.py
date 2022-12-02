# # Simple Calculator
# def add(n1, n2):
#     return n1 + n2

# def divide(n1, n2):
#     return n1 / n2

# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# calc_list = {
#     "+": add,
#     "/": divide,
#     "-": substract,
#     "*": multiply
# }
# def calculator():
#     num1 = float(input("What is the first number? "))
#     for key in calc_list:
#         print(key)

#     while True:
#         operation = input('Please select an operator: ')
#         num2 = float(input("What is the next number? "))
#         oper = calc_list[operation]
#         answer = oper(num1, num2)
#         print(f"{num1} {operation} {num2} = {answer}")
#         question = input(f"Type 'y' to continue calculating with {answer}, or type'n' to exit, or type 's' to start new calculator: ")
#         if question == 'y':
#             num1 = answer
#             continue
#         elif question == 's':
#             calculator()
#         else:
#             break

# calculator()

class Calculator:
    def __init__(self):
        self.num1 = float(input("What is the first number? "))
        self.num2 = float(input("What is the next number? "))
        
    def substruction(self):
        return self.num1 - self.num2
    
    def sum(self):
        return self.num1 + self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def calculation(self, n1, n2):
        self.calc_opertors = ['+', '-', '*', '/']
        self.operation = input(f"Please select an operation {self.calc_operators} ")

if __name__ == "__main__":
    my_calc= Calculator()
    my_calc.calculation(5, 3)



