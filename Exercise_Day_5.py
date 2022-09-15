# name = input('Please enter your name! ')

# print(name)
# conv_name = name[::-1].lower()
# print(conv_name.capitalize())


## Exercise Nr.2 Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***

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
    # clear()

    if guess in display_list:
        print(f"You have already guessed {guess}!")

    for position in range(text_length):
        letter = text[position]

        if letter == guess:
            display_list[position] = letter    

    print(display_list)

    if star not in display_list:
        end_of_game = True
        print("You win!")



# In principle, this is a good start to the game of hangman.


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