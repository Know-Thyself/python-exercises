from ascii_art import logo

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

print(logo)


def caesar(message, option, amount):
    caesar_message = ""
    alphabet_length = len(alphabet)
    if amount > 26:
        print("Invalid shift number! Please try again.")
        exit()
    if option == "decode":
        amount *= -1
        alphabet_length *= -1
    for char in message:
        if char in alphabet:
            current_index = alphabet.index(char)
            new_index = current_index + amount
            if new_index > 25 or new_index < 0:
                new_index = current_index + amount + alphabet_length
            char = alphabet[new_index]
        caesar_message += char
    print(f"The {option}d message is {caesar_message}")


repeat_task = True
while repeat_task:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number between 1 and 25:\n"))
    caesar(text, direction, shift)
    restart = input(
        'Would you like to encode/decode more messages? Please type "yes" or '
        '"no"\n'
    )
    if restart == "no":
        repeat_task = False
        print("Thanks for using Caesar Decipher!\nGoodbye!")
