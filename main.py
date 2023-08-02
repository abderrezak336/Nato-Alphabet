import pandas

#read the csv file
nato_phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#write your name
word = input("Your name please: ").upper()


# get each row in csv and turn it into dict
data_dictionaries = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_data.iterrows()}

# list of your name alphabet
final_list = [data_dictionaries[item] for item in word]

print(final_list)






