import Secret_auction_program_art

print(Secret_auction_program_art.logo)
print('Welcome to the secret auction program.')


def auction_winner():
    best_bid = 0
    winner_name = ''
    for bidder in auction_house:
        bidder_bid = auction_house[bidder]
        if best_bid < bidder_bid:
            best_bid = bidder_bid
            winner_name = bidder
    print(f'The winner is {winner_name} with a bid of ${best_bid}')


auction_house = {}
auction_entry = True
while auction_entry:
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))
    auction_house[name] = bid
    other_bidders = input('Are there other bidders? Y/N ').lower()
    if other_bidders == 'y':
        print('\n' * 30)
    elif other_bidders == 'n':
        auction_entry = False
        print('\n' * 30)
        auction_winner()
