import Higher_Lower_Game_data
import random

data = Higher_Lower_Game_data.data  # dictionary


def option_data(pick):
    name = pick['name']
    description = pick['description']
    country = pick['country']
    if pick == pick_A:
        option = 'A'
        return (f'Compare {option}: {name}, a {description}, from {country}')
    elif pick == pick_B:
        option = 'B'
        return (f'Against {option}: {name}, a {description}, from {country}')



def option_followers(pick):
    return pick['follower_count']


def comparassion(followers_A, followers_B):
    if followers_A > followers_B:
        winner = pick_A
    elif followers_A < followers_B:
        winner = pick_B
    return winner


def choice():
    if player_choice == 'a':
        player_pick = pick_A
    elif player_choice == 'b':
        player_pick = pick_B
    return player_pick

score = 0
pick_A = random.choice(data)
loop = True
while loop:
    pick_B = random.choice(data)
    if pick_A != pick_B:
        followers_A = option_followers(pick_A)
        followers_B = option_followers(pick_B)
        print('\n'*30)
        print(Higher_Lower_Game_data.logo)
        if score > 0:
            print(f'You\'re right. Current score: {score}.')
        print(f'{option_data(pick_A)}\n{Higher_Lower_Game_data.vs}\n{option_data(pick_B)}')
        player_choice = input('Who has more followers?: A/B ').lower()
        if comparassion(followers_A, followers_B) == choice():
            score += 1
            pick_A = choice()
        else:
            print('\n' * 30)
            print(f'Wrong, you lose! Your final score: {score}')
            loop = False
