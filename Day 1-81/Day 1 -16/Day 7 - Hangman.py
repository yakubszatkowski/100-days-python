import random
import Hangman

print(Hangman.logo)
word_list = Hangman.word_list
chosen_word = random.choice(word_list)
# print(f'Chosen word is {chosen_word}')        # for testing
lives = 6
display = []
for blank in chosen_word:                       # for every letter in chosen_word it adds '_' to the list
    display += '_'

end_game = False
while not end_game:
    guess = input('Guess a letter.\n').lower()
    if guess in display:
        print('You\'ve already chosen this letter')
    for position in range(len(chosen_word)):    # creates a for loop where position is the number assigned to specific letters of chosen_word
        if chosen_word[position] == guess:      # if letter of specific position of the chosen_word matches the guess then:
            display[position] = guess           # replaces specific position of display (blank list) with the guessed letter
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_game = True
        print("You win.")
    elif guess not in chosen_word:
        lives -=1
        print(f'You guessed a letter {guess}, That\'s not in the word. You lose a life')
        print(Hangman.stages[lives])
        if lives == 0:
            end_game = True
            print('You lose')
