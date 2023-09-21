import pandas
data = pandas.read_csv("/Users/l.stylianou/Development/udemy/100-days-of-code/Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
nato_alpha_dict = { row.letter: row.code for (index, row) in data.iterrows() }
# print(nato_alpha_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
	word = input('Enter a word: ').upper()
	try:
		print([ nato_alpha_dict[letter] for letter in word])
	except KeyError:
		print("Sorry, only letters in the alphabet please.")
		generate_phonetic()

generate_phonetic()
