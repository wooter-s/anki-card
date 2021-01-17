import csv

import os
import shutil


def transform(origin_list):
    answer_count: int = int(origin_list[2])
    result = origin_list[0]
    holdplace = origin_list[1]
    for index in range(3, 3 + answer_count, 1):
        answer = origin_list[index]
        # 多张卡
        # result = result.replace('{' + answer + '}', '{{c' + str(index) + '::' + answer + '}}')
        # 一张卡
        result = result.replace(holdplace + answer, '{{c1' + '::' + answer + '}}')
    return [result]


def generate_dist(origin_path: str, dist_path: str) -> None:
    with open(origin_path, 'r') as origin_file:
        origin_csv_reader = csv.reader(origin_file)
        with open(dist_path, '+a') as dist_file:
            dist_csv_writer = csv.writer(dist_file)
            for origin_row in origin_csv_reader:
                dist_row = transform(origin_row)
                dist_csv_writer.writerow(dist_row)

print(os.listdir('./data'))
dir_list = os.listdir('./data')
shutil.rmtree('dist')
os.mkdir('dist')
for dir in dir_list:
    print(f'dir ----> {dir}')
    test = os.listdir('./data/' + dir)
    print(f'test ----> {test}')
    os.mkdir('./dist/' + dir)
    for file in test:
        generate_dist('./data/' + dir + '/' + file, './dist/' + dir + '/' + file)
# path_list = os.listdir('./data/js')
# if len(path_list) == 0:
#     print("html文件夹不存在文件")
#
# if not os.path.exists('data'):
#     os.mkdir('data')
# else:
#     shutil.rmtree('data')
#     os.mkdir('data')
#
# if not os.path.exists('dist'):
#     os.mkdir('dist')
# else:
#     shutil.rmtree('dist')
#     os.mkdir('dist')
#
# for path in path_list:
