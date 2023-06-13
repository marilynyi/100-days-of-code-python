import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)

average = data["temp"].mean()
print(average)

max = data["temp"].max()
print(max)

print(data.condition)

print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")