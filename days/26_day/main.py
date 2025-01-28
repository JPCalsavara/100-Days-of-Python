#List Comprehension

# new_list = [new_value for value in list if case]

# f1 = open("file1.txt")
# f2 = open("file2.txt")
#
# number1 = f1.readlines()
# number2 = f2.readlines()
#
# f1.close()
# f2.close()
#
# result = [int(n) for n in number1 if n in number2]
#
# print(result)

#Dictionary Comprehension

# new_dictionary = {new_key:new_value for item in list}
# new_dictionary = {new_key:new_value for (key,item) in dictionary.items() if case}

#Loop through dictionaries:
#for (key,value) in dictionary.item():

student_dict = {
    "students":["Ana","Bia","Carla"],
    "score": [45,80,65],
}


# for (key,value) in student_dict.items():
#     print(value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

#loop data frame
# for (key,value) in student_data_frame.items():
#     print(value)

# loop rows in data frama
for(index,row) in student_data_frame.iterrows():
    print(row.students)
    if row.students == "Ana":
        print(row.score)