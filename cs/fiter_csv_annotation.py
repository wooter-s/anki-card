import csv
# 过滤备注的信息
with open('./data/safe/index.csv') as file:
    # rdr = csv.DictReader(filter(lambda row: row[0] != '#', file))
    rdr = csv.reader(filter(lambda row: row[0] != '#', file))
    for row1 in rdr:
        print(f'row ----> {row1}')