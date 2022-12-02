from turtle import clear
import re
# write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string

name1 = input('Please enter a text! ').lower()
name2 = input('Please enter a text! ').lower()

count_list = ''

while True:
    for i in name2:
        
        if i not in count_list and i in name1[::]:
            count_list += str((i) + " " + str(name1.count(i)) + ",")
            count_list_split = count_list.split(',')
            alphab_list = ', '.join(sorted(count_list_split, key=str.lower))
           
    if len(count_list) == 0:
        print("None of characters are in the first string")
        break
    print(alphab_list[2:])
    break




## Exercise Nr.2 Hangman
## Exercise Nr.2 Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***

picture_1line = '-'*9 
picture_2line = '-'*2 + '+' + '-'*3 + '+'
picture_3line = ' '*2 + '|' + ' '*3 + '|'
picture_4line = ' '*2 + 'O' + ' '*3 + '|'
picture_5line = ' ' + '/' + '|' + '\\' + ' '*2 + '|'
picture_line5 = ' ' + '/' + '|' + ' '*3 + '|'
picture_6line = ' ' + '/' + ' ' + '\\' + ' '*2 + '|'
picture_7line = ' '*6 +'|'
picture_line6 = ' ' + '/' + ' '*4 + '|'
stage7 = (f'{picture_2line}\n{picture_3line}\n{picture_4line}\n{picture_5line}\n{picture_6line}\n{picture_7line}\n{picture_1line}')
stage6 = (f'{picture_2line}\n{picture_3line}\n{picture_4line}\n{picture_5line}\n{picture_line6}\n{picture_7line}\n{picture_1line}')
stage5 = (f'{picture_2line}\n{picture_3line}\n{picture_4line}\n{picture_5line}\n{picture_7line}\n{picture_7line}\n{picture_1line}')
stage4 = (f'{picture_2line}\n{picture_3line}\n{picture_4line}\n{picture_line5}\n{picture_7line}\n{picture_7line}\n{picture_1line}')
stage3 = (f'{picture_2line}\n{picture_3line}\n{picture_4line}\n{picture_7line}\n{picture_7line}\n{picture_7line}\n{picture_1line}')
stage2 = (f'{picture_2line}\n{picture_3line}\n{picture_7line}\n{picture_7line}\n{picture_7line}\n{picture_7line}\n{picture_1line}')
stage1 = (f'{picture_2line}\n{picture_7line}\n{picture_7line}\n{picture_7line}\n{picture_7line}\n{picture_7line}\n{picture_1line}')
stage = (stage7, stage6, stage5, stage4, stage3, stage2, stage1)

text = input('Please enter a text! ').lower()

star = '*'
guess_list = ''

for i in text:
    if i == ' ':
        guess_list += ' '
    else:
        guess_list += star
print(guess_list)

lives = 6
game_over = False

while not game_over:
    guess = input('Please enter a letter! ').lower()

    clear()     #to continue while loop

    for letter in text:
        if letter == guess:
            letter_index = [i.start() for i in re.finditer(letter, text)]
            
            for number in letter_index:
                guess_list =  guess_list[:number] + letter + guess_list[number + 1:]
            
    print(guess_list)
    
    if star not in guess_list:
        game_over = True
        print('Congratulions! You win!')

    if guess not in text:
        lives -= 1
        print('Wrong guess, try again!')
        print(stage[lives])
    
    if lives == 0:
        game_over = True
        print('Sorry, you lose')

    