import bs4
import os




def get_string_count(string):
    return len(string) > 0

#
# count = get_string_count("3")
# print(f'count ----> {count}')

# tiku.html
exampleFile = open('../dist-html/一站到底决赛题库.html', encoding="gbk")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# print(f'exampleSoup ----> {exampleSoup}')
content = exampleSoup.select('.con_main')
content_string = content[0].get_text()
string = content_string.split("\n")
print(f'string ----> {string}')
string = filter(get_string_count, string)
print(f'string ----> {string}')
for item in string:
    print(f'{item}')

title = exampleSoup.title.get_text()
ul = exampleSoup.select('.main_box .content_side .hd_side .hd_side_list li')

# for item in ul:
#     print(f'item ----> {item}')
#     print(f'item.a ----> {item.a["href"].replace("//", "")}')




# files = os.listdir('../dist-html/')
# print(f'files ----> {files}')
# page_set = set()
# for name in files:
#     page_set.add(name)
# print(f'page_set ----> {page_set}')