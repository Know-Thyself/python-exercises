from ascii_art import logo, vs
from data import game_data
import random


def game_setup():
    print(logo)
    first_option = random.choice(game_data)
    person1 = format_entries(first_option)
    print(f"Compare A: {person1}")
    print(vs)
    second_option = random.choice(game_data)
    person2 = format_entries(second_option)
    print(f"Against B: {person2}")
    answer = input("Who has more instagram followers? Type 'A' or 'B': ")
    if answer == "A":
        evaluate_answer(first_option, second_option)
    elif answer == "B":
        evaluate_answer(second_option, first_option)


def format_entries(entry):
    return f"{entry['name']}, {entry['description']}, {entry['country']}"

def evaluate_answer(entry1, entry2):
    if entry1['follower_count'] > entry2['follower_count']:
        print('Correct!')
    else:
        print('Incorrect!')


game_setup()
