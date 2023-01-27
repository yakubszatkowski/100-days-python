import csv

with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

for items in list_of_rows:
    for item in items:
        if "https" in item:
            print('ok')
        else:
            print(item)
