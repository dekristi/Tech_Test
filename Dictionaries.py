# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 

# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included

#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile


def get_char_count(text):
    my_dict = {}
    for char in text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

new_dict = get_char_count('hubba bubba')
print(new_dict)

from typing import Counter
my_counter = Counter('hubba bubba')
print(my_counter)

# Secret Auction Program

# from replit import clear
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print('Welcome to the secret auction program!')

bidder_dic = {}

while True:
    name = input('What is your name?: ')
    bid = input('What is your bid? $ ')
    bidders = input('Are there any other bidders? Type "yes" or "no": ').lower()
    
    bidder_dic[name] = int(bid)

    if bidders == 'yes':
        clear = lambda: os.system('cls')
        clear()
    else:
        clear = lambda: os.system('cls')
        clear()
        max_key = max(bidder_dic, key=bidder_dic.get)
        max_val = max(bidder_dic.values())
        print(f'The winner is {max_key} with a bid of ${max_val}')
        break