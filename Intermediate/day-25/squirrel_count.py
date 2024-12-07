import pandas

raw_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241207.csv")
fury_colors_list = raw_data["Primary Fur Color"].unique().tolist()
fury_colors_dict = {}
for color in fury_colors_list[1:]:
    fury_colors_dict[color] = len(raw_data[raw_data["Primary Fur Color"] == color])

# print(fury_colors_dict)

storing_data = {
    "Fur Color": fury_colors_list[1:],
    "Count": list(fury_colors_dict.values())
}

pandas.DataFrame(storing_data).to_csv("fury_color_count.csv")

print(pandas.read_csv("fury_color_count.csv"))