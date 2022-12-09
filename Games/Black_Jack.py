import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []

def dealer():
    return random.shuffle(cards)


dealer_cards = random.sample(cards, 2)
player_cards = random.sample(cards, 2)

def calculate_score(dr_cards):
    if sum(dr_cards) == 21:
        return 0
    if 11 in dr_cards and sum(dr_cards) > 21:
        dr_cards.remove(11)
        dr_cards.append(1)
    return sum(dr_cards) 

player_score = calculate_score(player_cards)
dealer_score = calculate_score(dealer_cards)

while dealer_score < 17 and dealer_score != 0:
    dealer_cards.append(random.choice(cards))
    dealer_score = calculate_score(dealer_cards)

while True:
    dealer()
    print(f'Player cards are: {player_cards}')
    print(f'Dealer card is: {dealer_cards[0]}')
    ask_player = input("Do you need another card, 'yes' or 'no'? ")

    if ask_player == 'yes':
        player_cards.append(random.choice(cards))
        player_score = calculate_score(player_cards)
        
    if ask_player == 'no':
   
        if player_score < 21 and player_score > dealer_score and dealer_score < 21:
            print('You win!')
            print(f'Dealer total score is: {dealer_score}')
            break
            
        elif player_score < 21 and dealer_score > 21:
            print('You win!')
            print(f'Dealer score is: {dealer_score}')
            break
            
        elif player_score == dealer_score:
            print(f'Dealer cards are: {dealer_cards} and total score is {dealer_score}')
            print(f'Your total score is {player_score}. It is a draw!')
            break

        elif player_score == 0 or dealer_score == 0:
            if player_score == 0:
                print('Player has Black Jack!')
                break
            if dealer_score == 0:
                print('Dealer has Black Jack!')
                break

        else:
            print('You lose')
            print(f'Dealer score is: {dealer_score}')
            break
