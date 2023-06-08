alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(message, option, amount):
    caesar_message = ""
    alphabet_length = len(alphabet)
    if option == "decode":
        amount *= -1
        alphabet_length *= -1
    for letter in message:
        current_index = alphabet.index(letter)
        new_index = new_index = current_index + amount
        if new_index > 25 or new_index < 0:
            new_index = current_index + amount + alphabet_length
        letter = alphabet[new_index]
        caesar_message += letter
    print(f"The {option}d message is {caesar_message}")


caesar(text, direction, shift)
