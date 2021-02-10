import pandas as pd
import json
import glob
import pandas as pd
import csv

# file = open("/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/healthcaremagic_dialogue_1.txt", "rt")
# data = file.read()
# words = data.split()

# print('Number of words in text file :', len(words))
# occurrences = data.count("id")
# print(f'There are a total of {occurrences} conversations in this file, we must add the other three files to get to 300k')


# readinag given csv file
# and creating dataframe
df = pd.read_csv("healthcaremagic_dialogue_1.txt", error_bad_lines=False, sep='delimiter', header=None)
df1 = pd.read_csv('hopefully.csv')
df.columns = ['id_col']
# def remove_space():
#     #this function will remove empty space from our textfile
#     import sys
#     with open("healthcaremagic_dialogue_1.txt") as f, open(
#             '/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/no_space_dialogue.txt', 'w') as outfile:
#         for line in f:
#             if not line.isspace():
#                 sys.stdout.write(line)
#                 outfile.write(line)
#     return True


# This gathers all words between "dialogue" and "id", thus only getting doctor, patient convos
# make an empty textfile and write output data to it.
# with open('no_space_dialogue.txt') as infile, open(
#         'Strictly_Patient_Doc.txt', 'w') as outfile:
#     copy = False
#     for line in infile:
#         if line.strip() == "Dialogue":
#             copy = True
#             continue
#         elif line.startswith('id='):
#             copy = False
#             continue
#         elif copy:
#             outfile.write(line)

def word_count():
    file = open("/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/no_space_dialogue.txt", "rt")
    data = file.read()
    words = data.split()

    print('Number of words in text file :', len(words))
    conversations = data.count("Patient:")
    print(f'There are a total of {conversations} conversations in this file, we must add the other three files to get to 300k')





input_file = open('Strictly_Patient_Doc.txt', 'r')
output_file = open('patient_convo3.csv', 'w')

reader = csv.reader(input_file, delimtier = 'Doctor:', quoting=csv.QUOTE_NONE)
writer = csv.writer(output_file)

for row in reader:
    writer.writerow(row)

input_file.close()
output_file.close()
