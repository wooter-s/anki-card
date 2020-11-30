import os
import shutil

from icourse163 import Icourse163

print(os.listdir('./html'))

path_list = os.listdir('./html')
if len(path_list) == 0:
    print("html文件夹不存在文件")

if not os.path.exists('data'):
    os.mkdir('data')
else:
    shutil.rmtree('data')
    os.mkdir('data')

if not os.path.exists('dist'):
    os.mkdir('dist')
else:
    shutil.rmtree('dist')
    os.mkdir('dist')

for path in path_list:
    icourse = Icourse163(path)
    icourse.get_data_from_html()
    icourse.generate_anki_card()