import bs4
import csv


class Icourse163:
    path = ''
    def __init__(self, path):
        self.path = path

    def get_data_from_html(self):
        exampleFile = open('html/' + self.path)
        exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
        elems = exampleSoup.select(".m-choiceQuestion")
        data = []
        for ele in elems:
            rowData = []
            titleElement = ele.select(".qaDescription")
            title = titleElement[0].get_text().replace(" ","")
            # 题目内容
            rowData.append(title)

            answer = ele.select('.f-f0.tt2')[0].get_text()
            # 先预制题目类型
            rowData.append('radio')

            choices = ele.select('.choices.f-cb')
            # 选择数量
            rowData.append(len(choices[0]))
            # 答案
            rowData.append(answer)
            for choice in choices[0]:
                option_first = choice.select('.optionCnt')[0]
                optionContent = option_first.get_text()

                # 如果没有选项内容，使用选项；这是判断题
                if not optionContent:
                    option = choice.select('.optionPos')[0].get_text().replace(".", "")
                    icon_class = option_first.span["class"][0]
                    if icon_class == 'u-icon-correct':
                        rowData.append('正确')
                    # elif option == 'u-icon-wrong':
                    #     rowData.append('错误')
                    else:
                        rowData.append("错误")
                    rowData[1] = 'tof'
                else:
                    rowData[1] = 'radio'
                    rowData.append(optionContent)
            data.append(rowData)

        print(f'len(icourse163) ----> {len(data)}')
        print(f'icourse163 -> {data}')

        with open('data/' + self.path + '.csv', 'a+') as file:
            csv_write = csv.writer(file)
            for rowData in data:
                csv_write.writerow(rowData)

    def generate_anki_card(self):
        with open('data/' + self.path + '.csv', 'r') as file:
            csv_reader = csv.reader(file)
            with open('dist/' + self.path + '.csv', 'a+') as dist:
                dist_write = csv.writer(dist)
                for item in csv_reader:
                    answerKey = item[3]
                    answerIndex = self.get_index(answerKey)
                    answer = item[answerIndex]
                    content = item[0]
                    if "______" in content:
                        content = content.replace("______", '{{c1::' + answer + '}}')
                    else:
                        content = content + '{{c1::' + answer + '}}'
                    answerCount = int(item[2])
                    # 答案放在第一个
                    distAnswer = '<div>' + answer + '</div>'
                    for index in range(4, 4 + answerCount, 1):
                        # 去掉答案重复的
                        if index == answerIndex:
                            continue
                        distAnswer = distAnswer + '<div>' + item[index] + '</div>'
                    distDataRow = [content, distAnswer]
                    dist_write.writerow(distDataRow)
                    print(f'distDataROw ----> {distDataRow}')

    def get_index(self, input):
        """
        :param input:
        :return:
        """
        map = {
            'A': 4,
            'a': 4,
            'B': 5,
            'b': 5,
            'C': 6,
            'c': 6,
            'D': 7,
            'd': 7,
            'E': 8,
            'e': 8,
            'F': 9,
            'f': 9,
        }
        return map.get(input, None)
# exampleFile = open('html/linear-table-test.htm')
#
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select(".m-choiceQuestion")


#
# icourse163 = []
# for ele in elems:
#     rowData = []
#     titleElement = ele.select(".qaDescription")
#     title = titleElement[0].get_text().replace(" ","")
#     # 题目内容
#     rowData.append(title)
#
#     answer = ele.select('.f-f0.tt2')[0].get_text()
#     # 先预制题目类型
#     rowData.append('radio')
#
#     choices = ele.select('.choices.f-cb')
#     # 选择数量
#     rowData.append(len(choices[0]))
#     # 答案
#     rowData.append(answer)
#     for choice in choices[0]:
#         optionContent = choice.select('.optionCnt')[0].get_text()
#
#         # 如果没有选项内容，使用选项；这是判断题
#         if not optionContent:
#             option = choice.select('.optionPos')[0].get_text().replace(".", "")
#             if option == 'A':
#                 rowData.append('正确')
#             elif option == 'B':
#                 rowData.append('错误')
#             else:
#                 rowData.append(option)
#             rowData[1] = 'tof'
#         else:
#             rowData[1] = 'radio'
#             rowData.append(optionContent)
#     icourse163.append(rowData)
#
# print(f'len(icourse163) ----> {len(icourse163)}')
# print(f'icourse163 -> {icourse163}')
#
# filePath = 'test.csv'
# with open(filePath, 'a+') as file:
#     csv_write = csv.writer(file)
#     for rowData in icourse163:
#         csv_write.writerow(rowData)