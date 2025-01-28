import pandas as pd

df = pd.read_csv("xuxa_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

choose_word = input("Digite a palavra: ").upper()
xuxa_word = []
for letter in choose_word:
    if letter == '\0':
        pass
    else:
        xuxa_word = [dictionary[letter] for letter in choose_word]
    # print(final_dict[letter])
    # nato_word.append(final_dict[letter])
print(xuxa_word)



