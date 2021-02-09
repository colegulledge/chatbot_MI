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
df = pd.read_csv("healthcaremagic_dialogue_1.txt", error_bad_lines=False,sep='delimiter', header=None)
df1 = pd.read_csv('hopefully.csv')
df.columns = ['id_col']
print(df.head(50))
print(df1.head(50))
This gathers all words between "patient" and "doctor"
with open('/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/healthcaremagic_dialogue_1.txt') as infile, open('/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/output.txt', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "Patient:":
            copy = True
            continue
        elif line.strip() == "Doctor:":
            copy = False
            continue
        elif copy:
            outfile.write(line)
with open('/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/healthcaremagic_dialogue_1.txt') as infile, open('/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/response_2.txt', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "Doctor:":
            copy = True
            continue
        elif line.strip() == "\n":
            copy = False
            continue
        elif copy:
            outfile.write(line)

# input_file = open('healthcaremagic_dialogue_1.txt', 'r')
# output_file = open('maybe.csv', 'w')
#
# reader = csv.reader(input_file, delimiter = ':', quoting=csv.QUOTE_NONE)
# writer = csv.writer(output_file)
#
# for row in reader:
#     writer.writerow(row)
#
# input_file.close()
# output_file.close()








