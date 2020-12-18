import csv
from enum import Enum
import os


class QType(Enum):
    FILL = 'fill'
    SELECT = 'select'
    QUESTION = 'question'


class EtractCsv:
    """
    处理CSV
    """
    input_directory_path = ''
    output_directory_path = ''

    def __init__(self, input_file_path: str, output_file_path: str):
        self.input_directory_path = input_file_path
        self.output_directory_path = output_file_path

    def run(self):
        """
        启动处理
        """
        # g = os.walk(self.input_directory_path)
        # for path, dir_list, file_list in g:
        #     print('--->', path, dir_list, file_list)
        #     for file_name in file_list:
        #         origin_file_path = os.path.join(path, file_name)
        #         output_file_path = os.path.join(self.output_directory_path, file_name)
        #         print(f'origin_file_path ----> {origin_file_path}')
        #         print(f'output_file_path ----> {output_file_path}')
        #
        self.traverse_file(self.input_directory_path, self.output_directory_path)

    def _dispatch_file_handle(self, file_name: str, input_path: str, output_path: str):
        """

        :param file_name:
        :param input_path:
        """
        file_name_split = file_name.split('.')
        # 取倒数第二个后缀
        file_prefix = file_name_split[len(file_name_split) - 2]
        if file_prefix == QType.SELECT.value:
            print('操作选择题', file_name)
            self._process_select(file_name)
        if file_prefix == QType.FILL.value:
            print('操作填空题', file_name)
            self._handle_csv(input_path, output_path, self._process_fill)
        if file_prefix == QType.QUESTION.value:
            print('操作问答题', file_name)
            self._handle_csv(input_path, output_path, self._process_question)

    def traverse_file(self, input_directory: str, output_directory: str):
        """
        遍历文件
        """
        file_list = os.listdir(input_directory)
        for file_name in file_list:
            file_path = os.path.join(input_directory, file_name)
            output_path = os.path.join(output_directory, file_name)
            if os.path.isdir(file_path):
                # 如果不存在创建文件夹
                if not os.path.exists(output_path):
                    os.mkdir(output_path)
                self.traverse_file(file_path, output_path)
            else:
                # 处理文件
                self._dispatch_file_handle(file_name, file_path, output_path)
    # def handle_file(self):
    #     """
    #     处理文件
    #     """
    #     with open(self.input_directory_path) as file:
    #         csv_reader = csv.reader(file)
    #         for row in csv_reader:
    #             if row[1] == Q_type.SELECT:
    #                 print(1)

    def _process_select(self, file_path: str):
        """
        处理选择题
        """

    def _process_fill(self, item):
        """
        处理填空题
        """
        answer_count: int = int(item[1])
        result = item[0]
        for index in range(2, 2 + answer_count, 1):
            answer = item[index]
            # 多张卡
            # result = result.replace('{' + answer + '}', '{{c' + str(index) + '::' + answer + '}}')
            # 一张卡
            result = result.replace(answer, '{{c1' + '::' + answer + '}}')
        return [result]

    def _process_question(self, item):
        """
        处理问答题
        """
        answer = item[1]
        content = item[0]
        content = content + '{{c1::' + answer + '}}'
        dist_data_row = [content]
        return dist_data_row

    def _handle_csv(self, file_path: str, output_path: str, callback):
        with open(file_path, 'r') as file:
            # 过滤掉csv备注的内容
            # csv_reader = csv.reader(file)
            csv_reader = csv.reader(filter(lambda row: row[0] != '#', file))
            with open(output_path, 'w') as dist:
                dist_write = csv.writer(dist)
                for item in csv_reader:
                    dist_data_row = callback(item)
                    dist_write.writerow(dist_data_row)
                    # print(f'dist_data_row ----> {dist_data_row}')


etc = EtractCsv('./data', './dist')
etc.run()