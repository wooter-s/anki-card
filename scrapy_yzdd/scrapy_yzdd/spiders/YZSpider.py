import scrapy
import bs4

class YZSpider(scrapy.Spider):
    name = "YZSpider"
    title_set=set()

    def start_requests(self):
        urls = [
            'https://www.xuexila.com/zhishi/yizhandaodi/tiku/32829.html',
            # 20130301
            'https://www.xuexila.com/zhishi/yizhandaodi/tiku/35358.html',
            # 20141225
            'https://www.xuexila.com/zhishi/yizhandaodi/tiku/57283.html',
            'https://www.xuexila.com/zhishi/yizhandaodi/tiku/57283.html',
            # 一站到底题目及答案大全.html
            'https://www.xuexila.com/zhishi/yizhandaodi/tiku/305907.html',
            #
            'https://www.xuexila.com/zhishi/yizhandaodi/tiku/359819.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        print(f'response.url ----> {response.url}')
        exampleSoup = bs4.BeautifulSoup(response.body, 'html.parser')
        title = exampleSoup.title.get_text()
        filename = f'html/{title}.html'
        if not (title in self.title_set):
            self.title_set.add(title)
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log(f'Saved file {filename}')
            # 右侧列表
            ul = exampleSoup.select('.main_box .content_side .hd_side .hd_side_list li')
            for item in ul:
                # next_page = item.a["href"].replace("//", "")
                next_page = item.a["href"]
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)