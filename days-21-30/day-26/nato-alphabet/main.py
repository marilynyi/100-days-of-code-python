import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (_, row) in file.iterrows()}
# print(nato_dict)

first_name = input("What is your first name? ").upper()
nato_name = [nato_dict[letter] for letter in first_name]
print(nato_name)