from morse_code_dictionary import morse_dict

text = 'hello there'

# character_list = ''
# for character in text:
#     if morse_dict.get(character) is None:
#         character_list += ' '
#     else:
#         character_list += morse_dict.get(character)

character_list = ''.join([morse_dict.get(character, ' ') for character in text])

print(character_list)
