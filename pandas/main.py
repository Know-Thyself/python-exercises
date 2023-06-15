import csv
import pandas

days_weather = []
with open("weather_data.csv") as weather_file:
    reader = csv.DictReader(weather_file)
    temperatures = []
    for row in reader:
        days_weather.append(row)
        temperatures.append(int(row['temp']))

weather_data = pandas.read_csv("weather_data.csv")
weather_data_dict = weather_data.to_dict()
# print(weather_data)

average_temp = weather_data['temp'].mean()
max_temp = weather_data['temp'].max()
# printing the entire row based on condition
# print(weather_data[weather_data.temp == max_temp])
# print(weather_data[weather_data.day == 'Tuesday'])

data_dict = {
    "students": ["David", "Amy", "James"],
    "scores": [90, 97, 98]
}

new_data_frame = pandas.DataFrame(data_dict)
new_data_frame.to_csv("students_data.csv")

nyc_squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(type(nyc_squirrel_data))
gray_squirrels_count = len(nyc_squirrel_data[nyc_squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(nyc_squirrel_data[nyc_squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(nyc_squirrel_data[nyc_squirrel_data["Primary Fur Color"] == "Black"])

extracted_dict = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
extracted_squirrel_df = pandas.DataFrame(extracted_dict)

extracted_squirrel_df.to_csv("extracted_squirrel.csv")
print(extracted_squirrel_df)
