import textwrap

text = 'HELLO I AM OKAY DUDE '

text_in_lines = textwrap.fill(text, 17).split('\n')


line_count = 0
for line in text_in_lines:
    line_count += 1
    print(line_count)
    for character in line:
        print(character)
