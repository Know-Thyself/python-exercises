import random
from hangman_words import word_list
from hangman_ascii_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for letter in range(word_length):
    display += "_"

print(logo)
print(f"Guess a {len(chosen_word)} letters long word by entering one letter at a time")
print(f"{' '.join(display)}")

# Setting the number of lives the user has according to the game's rule.
lives = 6

while "_" in display and lives > 0:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Please enter a lower case letter between a - z\n").lower()
    print(f"You have {lives} lives left")
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_length):
        letter = chosen_word[position]
        if display[position] == letter:
            print(f"You've already chosen the letter {letter}, try another letter")
        if letter == guess:
            display[position] = letter
            print(f"The letter you guessed, {guess}, is in the chosen word.")
    print(stages[lives])
    if guess not in chosen_word:
        lives -= 1
        print(
            f"The letter you guessed, {guess}, is not in the chosen word. You lose a life"
        )
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("Congratulations! You win!")
    elif lives == 0 and "_" in display:
        print(f"You lose! The chosen word was {chosen_word}")
        print(stages[lives])
