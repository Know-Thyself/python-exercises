
from art import logo
import os

print(logo)
bidders = {}

def add_bidder(name, amount):
    bidders[name] = amount
 
 
is_bidding_open = True
while is_bidding_open:
    bidder_name = input('Enter your name \n')
    bidding_amount = int(input('Enter your bid \n£'))
    add_bidder(bidder_name, bidding_amount)
    more_bidder = input('Are there more bidders? Please enter "yes" or "no"\n')
 
    if more_bidder == 'no':
        is_bidding_open = False
    else:
        os.system('cls')

winner = {}
highest_bid = 0
winner_name: str

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        winner_name = bidder
        winner = {winner_name: highest_bid}

print(f'The winner is {winner_name} and their bid was £{highest_bid}')