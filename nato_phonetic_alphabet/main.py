import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
name = list(input("What is your name: "))
new_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
nato_phonetic_name = [new_dict[letter.upper()] for letter in name if letter != ' ']
print(new_dict)

print(nato_phonetic_name)

