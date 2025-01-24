# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
# #
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     # print(data)
#     for row in data:
#         # if row[1] != "temp":
#     #         temperature.append(int(row[1]))
#             temperature.append(row)
#             print(row)
#     # print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["day"].to_list()
# print(temp_list)
#
# #Initial function with pandas
# print(data["temp"].mean())
# print(data["temp"].max())

#Get data from a columns
# print(data[data.condition])
# print(data[data["condition"]])

#Get data from a row
# print(data[data.temp == data.temp.max()])
# print(data.condition)

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "students":["Ana","Bia","Carla"],
#     "score":[60,90,45]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250124.csv")
fur_color = data["Primary Fur Color"].value_counts()
fur_color.to_csv("squirrel_data.csv")
# Final project

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250124.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count": [grey_squirrel,red_squirrel,black_squirrel]
}

df = pandas.DataFrame(data_dict)
print(df)
# df.to_csv("squirrel_count.csv")


