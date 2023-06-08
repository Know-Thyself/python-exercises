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


def encrypt(message, amount):
    ciphered_message = ""
    for letter in message:
        current_index = alphabet.index(letter)
        if current_index + amount > 25:
            new_index = (current_index + amount) - 26
            letter = alphabet[new_index]
        else:
            letter = alphabet[current_index + amount]
        ciphered_message += letter

    print(ciphered_message)


def decrypt(message, amount):
    deciphered_message = ""
    for letter in message:
        current_index = alphabet.index(letter)
        print(current_index)
        if current_index - amount < 0:
            new_index = (current_index - amount) + 26
            letter = alphabet[new_index]
        else:
            letter = alphabet[current_index - amount]
        deciphered_message += letter
    print(deciphered_message)


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
