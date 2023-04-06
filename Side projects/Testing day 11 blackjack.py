import random


def final_calculation(player_score, computer_score):
    if player_score > computer_score:
        print(f'You win!')
    elif player_score < computer_score:
        print(f'You lose!')
    elif player_score == computer_score:
        print(f'Draw!')
def dobieranie():
    computer_score += random.randint(1,6)
# start game
# start = input('Are you ready to start? Y/N ').lower()
start = 'y'
if start == 'y':
    loop = True
    while loop:
        player_score = 21; computer_score = 14                      #change here
        if player_score == 21 and computer_score == 21:
            print('Draw! (Pretty rare one honestly)')
            loop = False
        elif player_score == 21 or computer_score > 21:
            print('You win!')
            loop = False
        elif player_score > 21 or computer_score == 21:
            print('You lose!')
            loop = False
        else:

            final_calculation(player_score, computer_score)
            loop = False