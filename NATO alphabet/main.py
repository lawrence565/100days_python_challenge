# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas


#TODO 1. Create a dictionary in this format:
alphabet_file = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_file.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ").upper()
result_list = [alphabet_dict[letter] for letter in name]
print(result_list)

