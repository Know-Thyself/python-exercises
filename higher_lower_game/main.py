from ascii_art import logo, vs
from data import game_data
import random


def game_setup(first_option=random.choice(game_data), score=0):
    second_option = random.choice(game_data)
    print(logo)
    print(f"Compare A: {format_entries(first_option)}")
    print(vs)
    print(f"Against B: {format_entries(second_option)}")
    play(first_option, second_option, score)


def format_entries(entry):
    return f"{entry['name']}, {entry['description']}, {entry['country']}"


def play(entry1, entry2, score=0):
    print(f"Your current score is: {score}")
    answer = input("Who has more instagram followers? Type 'A' or 'B': ")
    if answer == "A":
        result = evaluate_answer(entry1, entry2, score)
    elif answer == "B":
        result = evaluate_answer(entry2, entry1, score)
    if result:
        current_score = score + 1
        game_setup(entry2, current_score)
    else:
        if input('Type "y" if you want to play again or "n" to exit: ') == "y":
            game_setup()


def evaluate_answer(entry1, entry2, score=0):
    if entry1["follower_count"] > entry2["follower_count"]:
        print(f"You're right! Your current score is: {score + 1}")
        return True
    else:
        print(f"Incorrect! Your score was {score}")
        return False


game_setup()
