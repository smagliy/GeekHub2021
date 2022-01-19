import datetime
from bs4 import BeautifulSoup
import scrapy
from ..items import NewsItem


class NewstoscrapeSpider(scrapy.Spider):
    name = 'newstoscrape'
    allowed_domains = ['vikka.ua']
    start_urls = [f'http://vikka.ua/']

    def start_requests(self):
        try:
            date = input('Write date (2019/05/09): ')
            d = datetime.datetime.strptime(date, '%Y/%m/%d')
            if (datetime.datetime.today() - d).days >= 0:
                url_news = f'https://www.vikka.ua/{date}/'
                yield scrapy.Request(
                    url=url_news,
                    callback=self.parse_first_page
                )
        except Exception:
            print('Data isn`t correct!')

    def parse_first_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        for l in soup.select('h2.title-cat-post a'):
            href = self.parse_url(l.get('href'))['href']
            yield scrapy.Request(
                url=href,
                callback=self.parse_posts
            )
        next_page = soup.select_one('a.next')
        if next_page is not None:
            print('No next page')
            next_page = next_page.get('href')
            yield scrapy.Request(
                url=next_page,
                callback=self.parse_first_page
            )

    def parse_url(self, href):
        dict_hrefs = {
            'href': href
        }
        return dict_hrefs

    def parse_posts(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        items = NewsItem()
        list_href = [el.get('href') for el in soup.select('link[rel="canonical"]')]
        list_tags = ["#" + el.text for el in soup.select('a.post-tag')]
        items['name_post'] = soup.select_one('h1').text
        items['texts'] = soup.select_one('div.entry-content.-margin-b').text
        items['tags'] = " ".join(list_tags)
        items['link'] = list_href[0]
        yield items

