import random

game_on = True
while game_on:
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
    secret_number = random.randint(1,100)
    #print(f'*ppst* The secret number is {secret_number}...')
    difficulty = input('Choose a difficulty. Type "easy or "hard": ')
    if difficulty == 'hard':
        print('You have 5 chances to guess the number.')
        lives = 5
    elif difficulty == 'easy':
        lives = 10
        print('You have 10 chances to guess the number.')
    while lives > 0:
        guess = int(input('Make a guess: '))
        if guess == secret_number:
            print(f'You got it! The number was {secret_number}')
            lives = 0
        else: #guess != secret_number:
            lives -= 1
            if guess > secret_number:
                print(f'Too high. You have {lives} left...')
            elif guess < secret_number:
                print(f'Too low. You have {lives} left...')
            else:
                print(f'That\'s not a number. You have {lives} left...')
            if lives == 0:
                print('You\'ve ran out of guesses, you lose.')
    else:
        restart = input('Do you want to play again? Y/N ').lower()
        if restart == 'n':
            game_on = False
        elif restart == 'y':
            print('\n'*30)

