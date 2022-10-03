card_suits = ['clubs ♣', 'diamonds ♦', 'hearts ♥', 'spades ♠']
card_face = ['A', 'K', 'Q', 'J']
cards = []

for i in card_suits:
    for j in card_face:
        cards.append(str(j) + ' ' + i)
print(cards)

        