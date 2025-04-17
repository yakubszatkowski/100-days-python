# # not related to project

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     # next(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature = int(row[1])
#             temperatures.append(temperature)
#
# print(temperatures)

import pandas

# Importing csv file to variable
data = pandas.read_csv('weather_data.csv')
# print(data)

# # Creating dictionary from variable
# data_dict = data.to_dict()
# print(data_dict)

# # Creating list of column values
# temp_list = data['temp'].to_list()
# print(temp_list)

# # Calculating mean/average
# print(sum(temp_list)/len(temp_list))
# print(data['temp'].mean())

# # Finding the max value in temp column
# max_temp = data['temp'].max()
# print(max_temp)

# # Getting data in columns
# print(data.temp) ; print(data['temp'])

# # Getting data in row of certain day of week
# print(data[data.day == 'Monday'])

# # Getting row with highest temperature value
# print(data[data.temp == data.temp.max()])
# # or        ^^^ checks which value equals to max value
# print(data[data.temp == data['temp'].max()])

# # Creating row variable and extracting value of condition column
# monday = data[data.day == 'Monday']
# print(monday.condition)

# # Getting monday's temperature in Fahrenheit
# print(int(monday.temp) * 9/5 + 32)

# # Creating a dataframe from scratch
# data_dictionary = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dictionary)
# # print(data)

# # Getting this dataframe to csv file
# data.to_csv('new_data')
