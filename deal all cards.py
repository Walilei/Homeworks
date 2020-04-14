import random

player_num = int(input('Enter player nums: '))
players = []
for player in range(1, player_num+1):
    players.append([])

cards = []
for suit in range(1, 5):
    if suit == 1:
        for rank in range(1, 14):
            cards.append(('Spade', rank))
    elif suit == 2:
        for rank in range(1, 14):
            cards.append(('Heart', rank))
    elif suit == 3:
        for rank in range(1, 14):
            cards.append(('Diamond', rank))
    elif suit == 4:
        for rank in range(1, 14):
            cards.append(('Club', rank))


def deal_cards(person, people_nums):
    cards_on_hand = 52 // people_nums
    for i in person:
        for j in range(cards_on_hand):
            card = random.choice(cards)
            i.append(card)
            cards.remove(card)


deal_cards(players, player_num)

for idx in range(player_num):
    print(f"Player{idx+1}\'s cards: {sorted(players[idx])}")
