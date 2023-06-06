import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for letter in range(word_length):
    display += "_"

print(f"{' '.join(display)}")
print(f"Guess a {len(chosen_word)} letters long word by entering one letter at a time")

# Setting the number of lives the user has.
lives = len(set(chosen_word))

while "_" in display and lives > 0:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    print(f"You have {lives} lives left")
    guess = input("Please enter a lower case letter between a - z\n").lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # If guess is not a letter in the chosen_word,Then reduce 'lives' by 1.
    lives -= 1
    print(f"{' '.join(display)}")
    if not "_" in display:
        print("Congratulations! You win!")
    elif lives == 0 and "_" in display:
        print("You lose!")