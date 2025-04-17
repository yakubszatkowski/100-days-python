import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato_alphabet)

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# # Based on that:
# pho_dict = {}
# for (index, row) in nato_alphabet.iterrows():
#     pho_dict[row.letter] = row.code

# # Done this:
pho_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def translate():
    user_input = input('Enter a word: ').upper()
    try:
        pho_word_list = [pho_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry only letters in the alphabet please.')
        translate()
    else:
        print(pho_word_list)


translate()
