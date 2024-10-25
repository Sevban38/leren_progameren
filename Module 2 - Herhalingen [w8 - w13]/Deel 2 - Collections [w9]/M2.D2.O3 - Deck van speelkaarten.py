import random

suits = ['Harten', 'Klaveren', 'Schoppen', 'Ruiten', 'vierkanten']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer', 'Aas', 'timmerman']
deck = [f'{rank} van {suit}' for suit in suits for rank in ranks] + ['Joker', 'Joker']

random.shuffle(deck)
hand = deck[:7]
remaining_deck = deck[7:]

print("Bovenste 7 kaarten:", hand)
print("Overgebleven kaarten:", remaining_deck)
print("Aantal overgebleven kaarten:", len(remaining_deck))