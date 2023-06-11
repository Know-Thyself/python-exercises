from art import logo
import os

print(logo)
bidders = {}


def add_bidder(name, amount):
    bidders[name] = amount


def select_winner(participants):
    highest_bid = 0
    winner_name: str
    for bidder in participants:
        if participants[bidder] > highest_bid:
            highest_bid = participants[bidder]
            winner_name = bidder
    print(f'The winner is {winner_name} and their bid was £{highest_bid}')


is_bidding_open = True
while is_bidding_open:
    bidder_name = input('Enter your name \n')
    bidding_amount = int(input('Enter your bid \n£'))
    add_bidder(bidder_name, bidding_amount)
    more_bidder = input('Are there more bidders? Please enter "yes" or "no"\n')

    if more_bidder == 'no':
        is_bidding_open = False
        select_winner(bidders)
    else:
        os.system('cls')
