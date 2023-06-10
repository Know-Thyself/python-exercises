from ascii_art import logo
import random


def choose_difficulty():
    level = input('Type "easy" or "hard" to choose a difficulty level: ')
    if level == "hard":
        print("You've 5 guesses to find the correct number")
        return 5
    else:
        print("You've 10 guesses to find the correct number")
        return 10


def compare_numbers(num1, num2, attempts):
    if num1 == num2:
        print(f"You win! You guessed the number {num1} correctly!")
        restart_game()
    elif attempts - 1 == 0:
        print("You've run out of guesses, You lose!")
        restart_game()
    elif num2 > num1:
        print(f"Too high! Try a lower number\n You've {attempts - 1} guesses left")
    else:
        print(f"Too low! Try a higher number\n You've {attempts - 1} guesses left")


def guess_a_number():
    print("Welcome to the Number Guessing Game!")
    print(logo)
    number_of_guesses = choose_difficulty()
    chosen_number = random.randint(1, 100)

    while number_of_guesses > 0:
        guess = int(input("Type a positive integer between 1 and 100: "))
        compare_numbers(chosen_number, guess, number_of_guesses)
        number_of_guesses -= 1
        if chosen_number == guess:
            return


def restart_game():
    play_again = input('Type "y" to play again  or "n" to exit: ')
    if play_again == 'y':
        guess_a_number()


guess_a_number()
