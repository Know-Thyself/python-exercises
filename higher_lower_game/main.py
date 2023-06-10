from ascii_art import logo, vs
from data import accounts
import random


def game_setup(account1=random.choice(accounts), score=0):
    account2 = random.choice([i for i in accounts if i != account1])
    print(logo)
    print(f"Compare A: {format_entries(account1)}")
    print(vs)
    print(f"Against B: {format_entries(account2)}")
    play(account1, account2, score)


def format_entries(account):
    return f"{account['name']}, {account['description']}, {account['country']}"


def play(entry1, entry2, score=0):
    print(f"Your current score is: {score}")
    answer = input("Who has more instagram followers? Type 'A/a' or 'B/b': ").lower()
    if answer == "a":
        result = evaluate_answer(entry1, entry2, score)
    elif answer == "b":
        result = evaluate_answer(entry2, entry1, score)
    if result:
        current_score = score + 1
        game_setup(entry2, current_score)
    else:
        shall_play_again = input(
            'Type "Y/y" if you want to play again or "N/n" to exit: '
        ).lower()
        if shall_play_again == "y":
            game_setup()


def evaluate_answer(entry1, entry2, score=0):
    if entry1["follower_count"] > entry2["follower_count"]:
        print(
            f"You're right! {entry1['name']} has more followers than {entry2['name']}."
        )
        return True
    else:
        print(
            f"Incorrect! {entry2['name']} has more followers. \nYour score was {score}"
        )
        return False


game_setup()
