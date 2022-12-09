import random
logo = """
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
"""
# print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100!")
diffic = input('Choose a difficulty. Type "easy" or "hard": ')

attempt = 0
if diffic == 'easy':
    attempt = 10

if diffic == 'hard':
    attempt = 5

num = random.randrange(1, 101)
# print(num)

game_over = False

while not game_over:
    print(f'You have {attempt} attempts remaining to guess a number!')
    guess = int(input('Make a guess: '))
    if guess > num and attempt > 1 and guess != num:
        attempt -= 1
        print('Too high!')
    elif guess < num and attempt > 1 and guess != num:
        attempt -= 1
        print('Too low!')
    elif attempt == 1:
        print('You lose')
        game_over = True
    else:
        print('You guess a number!')
        game_over = True





