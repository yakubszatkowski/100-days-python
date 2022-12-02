import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_count = data['Primary Fur Color'].value_counts()
gray_count = fur_count[0]
red_count = fur_count[1]
black_count = fur_count[2]

datadict = {
    'Fur Color': ['gray', 'red', 'black'],
    'Count': [gray_count, red_count, black_count],
}

df = pandas.DataFrame(datadict)
df.to_csv('squirrel_count')

