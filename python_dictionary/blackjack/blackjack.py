import random
from art import logo
import os

print(logo)
print("Welcome to Blackjack Game!")


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(list_of_cards)
    if score == 21 and len(list_of_cards) == 2:
        return 0
    elif 11 in list_of_cards and score > 21:
        list_of_cards[list_of_cards.index(11)] = 1
    return score


def determine_winner(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "You Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = 0
    user_score = 0

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(
        f" Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(determine_winner(user_score, computer_score))


is_game_started = False
start = input("Type 'y' to start the game, type 'n' to exit\n:")
while start == "y":
    is_game_started = True
    play_blackjack()
    os.system('cls')
