student_dict = {
    "student" : ["Angela","James", "Lilly"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)
    
import pandas

data = pandas.DataFrame(student_dict)
# print(data)

#Loop through a data frame
# for (key, value) in data.items():
#     print(key)
#     print(value)

#Loop through rows of a data frame
for (index, row) in data.iterrows():
    print(row.student)