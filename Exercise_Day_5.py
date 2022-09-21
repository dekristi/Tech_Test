# # The user enters a name.
#
# You print user name in reverse (should begin with capital letter)
# then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"
#
# Example:
#
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?
# 
name = input('Please enter your name! ')
print(name)
conv_name = name[::-1].lower()
print(f'{conv_name.capitalize()}, a thorough mess is it not {name[0].upper()}')


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

lives = 6

text = input('Please enter a text ').lower()
display_list = []
text_length = len(text)

star = '*'

for i in text:
    display_list += star
print(display_list)

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter!: ").lower()
    
    if guess in display_list:
        print(f"You have already guessed {guess}!")

    for position in range(text_length):
        letter = text[position]

        if letter == guess:
            display_list[position] = letter    

    print(display_list)

    if letter != guess:
        lives -= 1
        print('You did not guess, please try again!')
        print(stage[lives])

    if star not in display_list:
        end_of_game = True
        print("You win!")



# 3. Text conversion

# Write a program for text conversion

# Save user input

# Print the entered text without changes

# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good

# Examples:

# The weather is not bad -> The weather is good

# The car is not new -> The car is not new

# This cottage cheese is not so bad -> This cottage cheese is good 

# Hints:

# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.

# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?

sentence = input('Please enter your sentence! ')
print(sentence)
spl_sentence = sentence.split()

new_sentence =''

if 'not' and 'bad'  in spl_sentence:
    not_index = spl_sentence.index('not')
    bad_index = spl_sentence.index('bad')
    new_sentence = (' '.join(spl_sentence[:not_index]) + ' good ' + ' '.join(spl_sentence[bad_index + 1:]))
else:
    new_sentence == sentence
print(new_sentence)


    
    