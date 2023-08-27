# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	print(data)
# 	for row in data:
# 		value = row[1]
# 		if value.isnumeric():
# 			temperatures.append(int(value))
		
# 	print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"].to_list())
print(f"Average temperature is {data['temp'].mean()}")
print(f"Max temperature is {data['temp'].max()}")

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

students = pandas.DataFrame(data_dict)
print(students)

students.to_csv("student_data.csv", index= False)