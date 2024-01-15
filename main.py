# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     # print(key, value)
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     Access index and row
#     print(row)
#
#     #Access row.student or row.score
#     print(row.student, row.score)
#     pass


#TODO 1. Create a dictionary in this format:
import pandas
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# print(data_dict)

# name_code = [data.loc(letters) for letters in name]
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name to know the code: ")

name_code = [data_dict[letter.upper()] for letter in name]

print(name_code)
