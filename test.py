from turtle import clear
num_list = []
prime_num = False
while True:
    numbers = int(input('How much first prime numbers you want to know? '))
    max_num = numbers**3
    clear()

    
    for i in range(2, max_num):
        if i > 0:
            for num in range(2, max_num):
                               
                if i % num == 0 and i != num:
                    break
                if i <= num:
                    break
           
                else:
                    if i not in num_list:
                        num_list.append(i)
#                 # if i % num != 0 and i % 2 != 0:
#                 #     if i not in num_list:
#                 #         num_list.append(i)
    print(num_list)
    print(f'First {numbers} prime numbers are: {num_list[:numbers]}')
    break
# Program to check if a number is prime or not

# num = 21

# flag = False

# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")