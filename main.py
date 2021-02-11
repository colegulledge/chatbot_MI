from pandas import DataFrame
#I dont believe we need this remove space, but it is still good to document just in case. 
def remove_space(file):
    #this function will remove empty space from our textfile
    import sys
    with open(file) as f, open(
            '/Users/colegulledge/Desktop/SPURSTECH/python_chatbot/no_space_dialogue_2nd_file.txt', 'w') as outfile:
        for line in f:
            if not line.isspace():
                sys.stdout.write(line)
                outfile.write(line)
    return True



#This gathers all words between "dialogue" and "id", thus only getting doctor, patient convos
#make an empty textfile and write output data to it.
def patient_doc_convo(file):
    with open(file) as infile, open('textfile3_cleaned_uneven_pat_doc.txt', 'w') as outfile:
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
def patient_doctor_count(file):
    file = open(file, "rt")
    data = file.read()
    list_result = data.split("Patient:")
    length_list = (len(list_result))
    print(f'The are a total of {length_list} Q and As')
    doctor_cnt = (data.count("Doctor:"))
    print(f'There are total of {doctor_cnt} Doctors:')
    patient_cnt = (data.count("Patient:"))
    print(f'There are a total of {patient_cnt} Patients:')

#Remove whitespaces and split on doctor into individual elements.. waiting for proper clean before
##we do so.
def split_doctors():
    new_list = []
    for el in list_result:
        #x = el.strip()
        x = el.replace('\n' , '')
        y = x.split('Doctor:')
        new_list.append(y)

#Push to Pandas dataframe and check for null values
##this will be the conclusion and ready for analysis, if proven there are no null values.

# df1 = DataFrame(new_list,columns=['Question','Answer'])
# df1.drop(df1.index[:1], inplace=True)
# print(df1)
# print((df1.isna().sum()))
