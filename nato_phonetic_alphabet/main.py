import pandas
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}


def generate_nato_phonetic_words():
    name = list(input("What is your name: "))
    try:
        nato_phonetic_name = [new_dict[letter.upper()] for letter in name if letter != ' ']
    except KeyError:
        print("Sorry, only names with English alphabet can be used")
        generate_nato_phonetic_words()
    else:
        print(nato_phonetic_name)
    finally:
        more_names = input("Would you like to go again? Type 'y' for yes or 'n' for no: ")
        if more_names == "y":
            generate_nato_phonetic_words()


generate_nato_phonetic_words()

