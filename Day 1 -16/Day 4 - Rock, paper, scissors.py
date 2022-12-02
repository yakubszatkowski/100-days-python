rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computerchoice = random.randint(0, 2)
list = ['rock', 'paper', 'scissors']
picturelist = [rock, paper, scissors]

if choice < 0 or choice > 2:
    print('Invalid number')
else:
    print(
        f'You\'ve chosen {list[choice]}\n{picturelist[choice]} \nand computer choose {list[computerchoice]}.\n{picturelist[computerchoice]} ')
    if choice == 2 and computerchoice == 0:
        print('You lose.')
    elif choice == 0 and computerchoice == 2:
        print('You win.')
    elif choice < computerchoice:
        print('You lose.')
    elif choice > computerchoice:
        print('You win.')
    elif choice == computerchoice:  # or else
        print('Draw.')
