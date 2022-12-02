import Ceaser_Cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'square', 'u', 'v', 'w', 'raw_data', 'y', 'z']
print(Ceaser_Cipher_art.logo)

def ceasar(text, shift, direction):
        if direction == 'decode':
            shift *= (-1)
        final_text=''
        for char in text:
            if char in alphabet:                          # allows only letters in alphabet to be changed
                position = alphabet.index(char)           # variable that determines the position of looped char from the text in the alphabet
                new_position = (position + shift) % 26    # creates new variable with shifted position. % 26 if too big shift number
                final_text += alphabet[new_position]      # adds char with shifted position to encrypted_text
            else:
                final_text += char                        # different characters others than char are added as normal
        print(f'The {direction}d text is: {final_text}')

end_of_game = False                                       # i'd rather to use function
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text,shift,direction)

    again = input('Do you want to restart cipher program? Type Y/N ').lower()
    if again == 'n':
        end_of_game = True
