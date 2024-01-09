import random

global deck_of_cards
dealer = []
player = []

deck_of_cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

player_card = deck_of_cards.pop(random.randint(0, len(deck_of_cards) - 1))
dealer_card = deck_of_cards.pop(random.randint(0, len(deck_of_cards) - 1))
print('player card',player_card)
print('dealder card',dealer_card)
player.append(player_card)
dealer.append(dealer_card)


def blackjack(hand):
    return 'A' in hand and (10 in hand or 'J' in hand or 'Q' in hand or 'K' in hand)

def calculate_hand_value(hand):
    value = 0
    num_a = hand.count('A')
    for card in hand:
        if card in ['J','Q','K']:
            value += 10
        elif card == 'A':
            value += 11
        else:
            value += int(card)
    while value > 21 and num_a > 0:
        value -= 10
        num_a -= 1
    return value

addition_card = deck_of_cards.pop(random.randint(0, len(deck_of_cards) - 1))
print('player draw card',addition_card)
player.append(addition_card)

if calculate_hand_value(player) > 21:
    print("Dealer wins.",'player card:',calculate_hand_value(player))
else:
    if calculate_hand_value(dealer) <= 16:
        card = deck_of_cards.pop(random.randint(0, len(deck_of_cards) - 1))
        print("dealer draw card",card)
        dealer.append(card)
    #print(calculate_hand_value(dealer))
    #print(calculate_hand_value(player))
    if calculate_hand_value(dealer) > 21:
        print("Player wins",'dealer card value:',calculate_hand_value(dealer))
    elif blackjack(player) and not blackjack(dealer):
        print("Player wins")
    elif calculate_hand_value(player) > calculate_hand_value(dealer):
        print("Player wins",'player card value:',calculate_hand_value(player),\
              'dealer card value:',calculate_hand_value(dealer))
    elif blackjack(dealer) and not blackjack(player):
        print("Dealer wins")
    elif calculate_hand_value(player) < calculate_hand_value(dealer):
        print("Dealer wins",'player card value:',calculate_hand_value(player),\
              'dealer card value:',calculate_hand_value(dealer))
    else:
        print("Dealer wins")
