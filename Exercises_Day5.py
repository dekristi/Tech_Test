# Exercise Nr 1 'FizzBuzz'

# range_list = ''

# for i in range(101):
#     if i % 5 == 0:
#         range_list += 'Fizz, '
#     elif i % 7 == 0:
#         range_list += 'Buzz, '
#     elif i % 7 == 0 and i % 5 == 0:
#         range_list += 'FizzBuzz, '
#     elif not (i % 7 ==0 and i % 5 == 0):
#         range_list += str(i) + ', '
# print(range_list)

## Exercise Nr. 2 'Christmas tree'

# ask = input("Please enter the hight of the tree! ")

# height = int(round(float(ask), 0))
# stars = '*'
# space = ' '

# for i in range(height + 1):
#     print(space * (height - i - 1) + stars * (2 * i + 1))

### Exercise Nr 3 'Prime numbers'

prime_num = False

num = int(input('Please enter a numer! '))

if num > 0:
    for i in range(2, num):
        if num % i == 0:
            prime_num = True
            break
if prime_num:       
    print(f'{num} is not a Prime number!')    
else:
    print(f'{num} is a prime number!')