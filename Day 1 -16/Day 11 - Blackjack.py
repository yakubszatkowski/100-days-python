import random
import Blackjack_art


cards = {
    'Ace': 11,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}


def random_card():
    return random.choice(list(cards.items()))


def deal_card(player_hand, computer_hand, player_hit, computer_hit):
    if computer_hit == True:
        computer_hand += random_card()
    if player_hit == True:
        player_hand += random_card()


def calculate_score(hand):
    total_score = 0
    for score in range(1, len(hand), 2):
        total_score += hand[score]
        if 'Ace' in hand and total_score > 21:  # THIS WAS HARD TO FIGURE OUT
            total_score -= 10
    return total_score


def hand(hand):
    total_hand = []
    for card in range(0, len(hand), 2):
        total_hand.append(hand[card])
    return total_hand


def final_calculation(player_score, computer_score, player_hand2, computer_hand2):
    if player_score > computer_score:
        print(f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {computer_hand2}\nYou win!')
    elif player_score < computer_score:
        print(f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {computer_hand2}\nYou lose!')
    elif player_score == computer_score:
        print(f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {computer_hand2}\nDraw!')

print(Blackjack_art.logo)
start = input('Are you ready to start? Y/N ').lower()
if start == 'y':
    player_hand = []
    computer_hand = []
    deal_card(player_hand, computer_hand, player_hit=True, computer_hit=True)
    deal_card(player_hand, computer_hand, player_hit=True, computer_hit=True)
    loop = True
    while loop:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        player_hand2 = ', '.join(hand(player_hand))
        computer_hand2 = ', '.join(hand(computer_hand))
        if player_score == 21 and computer_score == 21:
            print(f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {computer_hand2}\nDraw! (Pretty rare one honestly)')
            loop = False
        elif player_score == 21 or computer_score > 21:
            print(f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {computer_hand2}\nYou win!')
            loop = False
        elif player_score > 21 or computer_score == 21:
            print(f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {computer_hand2}\nYou lose!')
            loop = False

        else:
            print(
                f'\nYour hand consists of {player_hand2}.\nComputer hand consists of {hand(computer_hand)[0]}, and a hidden card.')
            hit = input('\nWould you like to draw a card? Y/N ').lower()
            if hit == 'y':
                deal_card(player_hand, computer_hand, player_hit=True, computer_hit=False)
            elif hit == 'n':
                while calculate_score(computer_hand) < 17:
                    deal_card(player_hand, computer_hand, player_hit=False, computer_hit=True)
                    computer_score = calculate_score(computer_hand)
                    computer_hand2 = ', '.join(hand(computer_hand))
                final_calculation(player_score, computer_score, player_hand2, computer_hand2)
                loop = False
