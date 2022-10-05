import random
import itertools as it

# 1. The Shuffle
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]
# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
# you can use a loop or use something from the library


# def get_shuffled_cards():
#     card_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10','A', 'K', 'Q', 'J' ]
#     card_suits = ['clubs ♣', 'diamonds ♦', 'hearts ♥', 'spades ♠']
    # cards = [(num, suit) for num in card_num for suit in card_suits] 
#     cards = list(it.product(card_num, card_suits))
#     random.shuffle(cards)
#     return cards
      
# print(get_shuffled_cards())

import itertools as it
import random

class Deck:
    available=52
    spent=0
    
    def __init__(self):
        
        self.card_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10','A', 'K', 'Q', 'J' ]
        self.card_suits = ['clubs ♣', 'diamonds ♦', 'hearts ♥', 'spades ♠']
        self.available_cards = list(it.product(self.card_num, self.card_suits))
        
    def card_deck(self):    
        return self.available_cards
    
    def shuffle(self):
        return random.shuffle(self.available_cards)
        
    def get_cards(self, count=1):
    
        if count <= Deck.available:
            Deck.available -= count
            Deck.spent += count
            self.available_cards = self.available_cards[count:]
            self.cards = self.available_cards[:count]
       
        print(f'The number of available cards are: {Deck.available}, you have spent {Deck.spent}')
        print(f'Your cards are {self.cards}')
        return self.cards

if __name__ == "__main__":
    my_deck = Deck()
    print(my_deck.available)
    print(my_deck.spent) 
    my_deck.shuffle() 
    print("You asked 5 cards")
    my_cards = my_deck.get_cards(5)
    my_deck.shuffle() 
    print('You asked a card')
    single_card = my_deck.get_cards()
    my_deck.shuffle()
    print('You asked 10 cards')
    my_cards = my_deck.get_cards(10)
