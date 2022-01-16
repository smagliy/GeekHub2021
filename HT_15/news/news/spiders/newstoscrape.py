import scrapy
import csv
import datetime
from bs4 import BeautifulSoup


class NewstoscrapeSpider(scrapy.Spider):
    name = 'newstoscrape'
    allowed_domains = ['vikka.ua']
    start_urls = ['http://vikka.ua/']
    data = input('Write date (2019/05/09): ')

    def start_requests(self):
        try:
            d = datetime.datetime.strptime(self.data, '%Y/%m/%d')
            if datetime.datetime.now().day - d.day >= 0:
                url_news = f'https://www.vikka.ua/{self.data}/'
                yield scrapy.Request(
                        url=url_news,
                        callback=self.parse_news_page
                    )
            else:
                print('Data in future!')
        except Exception:
            print('Data isn`t correct!')

    def parse_news_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        for news in soup.select('li.item-cat-post'):
            list_hrefs = [l.get('href') for l in news.select('h2.title-cat-post a')]
            for link in list_hrefs:
                yield scrapy.Request(
                        url=link,
                        callback=self.parse_post_page
                    )

    def parse_post_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        post = self.parse_post(soup, response)
        print(post)

    def parse_post(self, soup_post, link):
        dict_all = {
            'link': link,
            'name': soup_post.select_one('h1').text,
            'texts': [tex.text for tex in soup_post.select('div.entry-content p') if tex.text != ''],
            'tags': ['#'+tag.text for tag in soup_post.select('a.post-tag')]
        }
        fields = ['link', 'name', 'texts', 'tags']
        name = self.data.replace("/", "_")
        with open(f'{name}.csv', 'a+', encoding='utf-8') as f:
            file = csv.DictWriter(f, fields)
            file.writerow(dict_all)
        return dict_all



