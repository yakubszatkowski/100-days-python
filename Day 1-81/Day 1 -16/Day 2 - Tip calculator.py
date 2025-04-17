print('Welcome to the tip calculator.\n')
bill = float(input('What was the total bill? $'))
percentage = 1 + int(input('What percentage tip would you like to give? 10, 12 or 15? '))/100
people = int(input('How many people to split the bill? '))

split = bill * percentage / people
split = '{:.2f}'.format(split) #different than round
print(f'Each person should pay: ${split}.')
