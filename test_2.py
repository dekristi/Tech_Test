import random

# 1. The Shuffle
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]
# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
# you can use a loop or use something from the library
# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html

def get_shuffled_cards():
    card_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10','A', 'K', 'Q', 'J' ]
    card_suits = ['clubs ♣', 'diamonds ♦', 'hearts ♥', 'spades ♠']
    cards = [(num, suit) for num in card_num for suit in card_suits] 
    random.shuffle(cards)
    return cards
   
print(get_shuffled_cards())