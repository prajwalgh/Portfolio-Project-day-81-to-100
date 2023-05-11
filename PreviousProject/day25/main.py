# with open("weather_data.csv","r") as weather:
#     l=list(weather.readlines())
#
# print(l)
# above code output is not desirable
# import csv
# with open("weather_data.csv",) as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(temperature)
# above code is fast but long thus we use panda
# below code does same as above code with less line of code thus we us pandas
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print("day..................")
# print(data["day"].describe())
# print("temp..................")
# print(data["temp"].describe())
# # print(data['temp'])
# temp_list = data["temp"].to_list()
# avg=sum(temp_list)/len(temp_list)
# print("average is ",avg)
# print("mean is",data["temp"].mean())
# # TODO funtion .max() to return max value in data series
# print(data["temp"].max())
# OR
# print(data.temp.max()
# #TODO function .argmax()to return max val index
# max_val_index=data["temp"].argmax()
# print(data["temp"][max_val_index])

# #TODO how to print a row in panda
# print(data[data.day=="Monday"])
# #print row with max temp
# print(data[data.temp==data.temp.max()])
# print("day with max temp :",data[data.temp==data.temp.max()].day)
# celsius  to  fahrenheit
# print(data.temp[data.day == "Monday"])
# print(data[data.day == "Monday"].temp)
# a = int(data[data.day == "Monday"].temp)
# f = (a * 1.8) + 32
# print("monday temp is  fahrenheit :", f)
# TODO how to make a new data farme , new csv file
# data_dic={
#     "name":["ram","raj","rhoit","raju"],
#     "mark":[2,3,4,5]
# }
# data=pandas.DataFrame(data_dic)
# data.to_csv("new_data.csv")
import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.head(50))
# color = data["Primary Fur Color"].to_list()
# black_count = 0
# cinnamon_count = 0
# gray_count = 0
# for i in range(len(color)):
#     if color[i] == "Black":
#         black_count += 1
#     elif color[i] == "Cinnamon":
#         cinnamon_count += 1
#     elif color[i] == "Gray":
#         gray_count += 1
# print(black_count, cinnamon_count, gray_count)
cinnamon_count=len(data[data["Primary Fur Color"]=="Cinnamon"])

black_count=len(data[data["Primary Fur Color"]=="Blank"])
gray_count=len(data[data["Primary Fur Color"]=="Gray"])
data_color = {
    "cinnamon": [cinnamon_count],
    "black": [black_count],
    "grey": [gray_count]
}
data_color_set={
    "Fur color":['cinnamon','black','grey'],
    "Count":[cinnamon_count,black_count,gray_count]
}
#data1 = pandas.DataFrame(data_color)
#data1.to_csv("data1.csv")
data4 = pandas.DataFrame(data_color_set)
data4.to_csv("data4.csv")
