# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
# temperatures = []
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"]) # Recognise the title and the data of the column

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [78, 82, 86]
}

data = pandas.DataFrame(data_dict)
data.to_csv("class_score.csv")