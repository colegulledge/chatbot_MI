from pandas import DataFrame
import numpy as np
import sys

#This gathers all words between "dialogue" and "id", thus only getting doctor, patient convos
#make an empty textfile and write output data to it.
def patient_doc_convo(file):
    with open(file) as infile, open('DESIRED_FILE_NAME', 'w') as outfile:
        copy = False
        for line in infile:
            if line.strip() == "Dialogue":
                copy = True
                continue
            elif line.startswith('id='):
                copy = False
                continue
            elif copy:
                outfile.write(line)
    return True

# From here, we split the file into a list on patient, thus creating a list array
## of each conversation, we then count the occurances of "Patient:" and "Doctor:"
## to ensure we have the same amount of question and answers for analysis.
##once confirmed, we pass the list into its pandas dataframe.
def patient_doctor_count(file):
    file = open(file, "rt")
    data = file.read()
    list_result = data.split("Patient:")

    doctor_cnt = (data.count("Doctor:"))
    print(f'There are total of {doctor_cnt} Doctors:')
    patient_cnt = (data.count("Patient:"))
    print(f'There are a total of {patient_cnt} Patients:')
    if doctor_cnt == patient_cnt:
        pass
    else:
        sys.exit("ahhh!!! Something is wrong with your dialogue!!, return and fix the errors,"
                 "try Hey Doctor: .. or refer to the log file and see what must"
                 "be hard removed..")

    new_list = []
    for el in list_result:

         x = el.replace('\n' , '')
         y = x.split('Doctor:')
         new_list.append(y)
    new_list.pop(0)

    length_new_list = (len(new_list))

    print(f'There are a total of {length_new_list} Q and As')

    df1 = DataFrame(new_list, columns=['Question', 'Answer'])
    df1.drop(df1.index[:1], inplace=True)

    #FIRST ROW IS NULL
    print((df1.isna().sum()))
    print(df1.head())


#patient_doctor_count('FINAL_TEXT_FILE2_CLEANED.txt')
#patient_doctor_count('FINAL_TEXT_FILE3_CLEANED.txt')
#patient_doctor_count('FINAL_TEXT_FILE2_CLEANED.txt')
#patient_doctor_count('FINAL_TEXT_FILE1_CLEANED.txt')
patient_doctor_count('MASTER_TEXT_FILE.txt')
