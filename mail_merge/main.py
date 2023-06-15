PLACEHOLDER = "[name]"

with open("./names/invited_names.txt") as names_file:
    # readlines() returns a list
    names = names_file.readlines()
with open("./letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        new_letter = letter.replace(PLACEHOLDER, name.strip())
        with open(f"./letters/letter_to_{name.strip()}.text", mode="w") as completed_letters:
            completed_letters.write(new_letter)

