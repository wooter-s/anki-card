import csv
from enum import Enum
import os

class Q_type(Enum):
    FILL = 'fill'
    SELECT = 'select'
    QUESTION = 'question'


print(Q_type.SELECT.value, Q_type.SELECT.value == 'select')
# class Etract_Csv:
#     def handle_file(path: str):
#         with open(path) as file:
#             csv_reader = csv.reader(file)
#             for row in csv_reader:
#                 if row[1] ==  Q_type.SELECT:
#                     print(1)
#
#     def handle
print(os.listdir('../base'))
# 判断最后第二个文件名类型
file_name_list = os.listdir('../base')
for file_name in file_name_list:
    file_name_split = file_name.split('.')
    # 取倒数第二个后缀
    file_prefix = file_name_split[len(file_name_split) - 2]
    if file_prefix == Q_type.SELECT.value:
        print('操作选择题')
    if file_prefix == Q_type.FILL.value:
        print('操作填空题')
    if file_prefix == Q_type.QUESTION.value:
        print('问答题')





