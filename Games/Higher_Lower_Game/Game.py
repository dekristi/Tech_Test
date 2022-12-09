import random
import os
from Game_Data import data
from Game_Logo import logo
from Game_Logo import vs

def game():
    a_choise = random.choice(data)
    b_choise = random.choice(data)
    while a_choise == b_choise:
        b_choise = random.choice(data)

    a_follow = a_choise['follower_count']
    b_follow = b_choise['follower_count']
    count = 0
    clear = lambda: os.system('cls')

    while True:
        print(logo)
        print(f"Compare A: {a_choise['name']}, a {a_choise['description']}, from {a_choise['country']}")

        print(vs)
        print(f"Compare B: {b_choise['name']}, a {b_choise['description']}, from {b_choise['country']}")
        # print(a_follow)
        # print(b_follow)
        quest = input("Who has more followeres? Type 'A' or 'B': ").lower()
        if a_follow > b_follow and quest == 'a':
            count += 1
            quest = True
            print(f"You are wright! Your score is {count}")
        elif a_follow < b_follow and quest == 'b':
            count += 1
            quest = True
            print(f"You are wright! Your score is {count}")
        else:
            quest = False

        if a_follow > b_follow and quest == True:
            clear()
            a_choise = a_choise
            b_choise = random.choice(data)
            continue
        elif a_follow < b_follow and quest == True:
            clear()
            a_choise = b_choise
            b_choise = random.choice(data)
            continue
        else:
            clear()
            print(f"You are wrong. Your score is {count}.")
            ask_quest = input('Do you want to play new game? Print "Yes" or "No": ').lower()
            if ask_quest == 'yes':
                game()
            else:
                break

game()
