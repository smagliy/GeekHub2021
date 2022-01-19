import scrapy


class NewsItem(scrapy.Item):
    name_post = scrapy.Field()
    texts = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
