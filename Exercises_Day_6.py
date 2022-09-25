 # 1a. Average value

# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.

from re import I
import statistics

spl_list = []
while True:
    numbers = input('Please enter numbers separated by comma! or "q" to quit ')

    spl_numbers = numbers.split(',')
    

    for num in spl_numbers:
        if num != 'q':          
            spl_list += [int(num)]
            avg_number = statistics.mean(spl_list)
            sort_list = sorted(spl_list)
            
    print(f'Entered numbers are: {spl_list}')
    print(f'Average of entered numbers is: {round(avg_number,2)}')
    print(f'Top 3 min numbers are: {sort_list[:3]}')
    print(f'Top 3 max numbers are: {sort_list[-3:]}')

    if num == 'q':
        print('You prefered to quit')
        break

# # 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]
start_num = int(input('Please enter a number! '))
end_num = int(input('Please enter another number!'))

num_list = []

for num in range(start_num, end_num + 1):
    cube_num = num**3
    num_list.append(cube_num)
    print(f'{num} cubed: {cube_num}')
print(f'All cubes are: {num_list}')

# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

sentence = input('Please enter a sentence! ').lower()

spl_sent = sentence.split(' ')
rev_list = []

for word in spl_sent:
    conv_word = word[::-1]
    rev_list.append(conv_word)
    rev_sent = ' '.join(rev_list)
print(rev_sent.capitalize())

# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise

prime_list = [2,]
num = int(input('How many prime numbers do you want to display? '))
start_num = 1

while True:
    prime_list_length = len(prime_list) 

    for i in range(2, start_num):
        if start_num % i == 0 and start_num in prime_list:
            # prime_list = [n.replace("start_num", "") for n in prime_list]
            prime_list = prime_list[:-1]

        if start_num % i == 0:
            break
    
        else:
            if start_num not in prime_list:
                prime_list.append(start_num)
    if prime_list_length < num:
        start_num += 1
    if prime_list_length == num:
        print(prime_list)
        break