import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

final_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

def generate_phonetic():
    choose_word = input("Enter a word: ").upper()

    try:
        nato_word = [final_dict[letter] for letter in choose_word]
    except KeyError:
        print("Oops, only letters in the alphabet,please")
        generate_phonetic()
    else:
        print(nato_word)

generate_phonetic()

