# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# didn't use hint 3


name_list = []
with open('./Input/Names/invited_names.txt', 'r') as name_file:
    extracted_list = name_file.readlines()
    for name in extracted_list:
        name_list.append(name.replace('\n', ''))

with open('./Input/Letters/starting_letter.txt') as starting_letter:
    content = starting_letter.read()

for name in name_list:
    with open(f'./Output/ReadyToSend/{name}_invitation.txt', mode='w') as invitation:
        invitation.write(content.replace('[name]', name))
