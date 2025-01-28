import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

final_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

choose_word = input("Enter a word: ").upper()
nato_word = []
for letter in choose_word:
    nato_word = [final_dict[letter] for letter in choose_word]
print(nato_word)



