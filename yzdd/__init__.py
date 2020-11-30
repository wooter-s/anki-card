import csv

with open('./data/20120309.csv', 'r') as file:
    csv_reader = csv.reader(file)
    with open('./dist/20120309.csv', 'a+') as dist:
        csv_write = csv.writer(dist)
        for row_data in csv_reader:
            content = row_data[0] + '{{c1::' + row_data[1] + '}}'
            csv_write.writerow([content, ''])