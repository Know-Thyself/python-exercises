# Password Generator Project
import random

letters = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_nums = random.sample(numbers, nr_numbers)
random_letters = random.sample(letters, nr_letters)
random_symbols = random.sample(symbols, nr_symbols)

random_password = random_letters + random_nums + random_symbols
generated_pw_str = "".join(random_password)
print(f"Your generated simple password is: {generated_pw_str}")
# Alternatively
# generated_pw_str = ""
# for char in random_password:
#     generated_pw_str += char
# print(generated_pw_str)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
mix_chars_list = random.sample(random_password, len(random_password))
generated_pw_str = "".join(mix_chars_list)
# Alternative solution
# generated_pw_str = ""
# for char in mix_chars_list:
#     generated_pw_str += char

print(f"Your generated more complex password is: {generated_pw_str}")
