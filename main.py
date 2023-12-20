# with open("weather_data.csv", "r") as weather_data:
#     data = []
#     for dates in weather_data.readlines():
#         data.append(dates.strip())
#     print(data)

# import csv # USING CSV
#
# with open("weather_data.csv", "r") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1].isdigit():
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_data = squirrels["Primary Fur Color"].value_counts()
color_data = color_data.to_dict()
print(color_data)





# # create a dictionary with lists containing colors
# squirrels_dict = {'Fur Color': ["Cinnamon", "Gray", "Black"],
#                   "Color Count": [squirrels["Primary Fur Color"].to_list().count("Cinnamon"),
#                                   squirrels["Primary Fur Color"].to_list().count("Gray"),
#                                   squirrels["Primary Fur Color"].to_list().count("Black")]}
#
# squirrels_df = pandas.DataFrame(squirrels_dict)
# try:
#     squirrels_df.to_csv("2018_squirrels")
#     print("CSV file created successfully.")
# except Exception as e:
#     print(f"Error: {e}")

# print(squirrels["Primary Fur Color"])