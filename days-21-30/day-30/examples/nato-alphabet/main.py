import pandas as pd

file = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (_, row) in file.iterrows()}
# print(nato_dict)

def name_to_nato():
    first_name = input("What is your first name? ").upper()
    try:
        nato_name = [nato_dict[letter] for letter in first_name]
    except KeyError:
        print("Invalid entry. Please input letters only.")
        name_to_nato()
    else:
        print(nato_name)

name_to_nato()

