import scrapy


class NavitimeSpider(scrapy.Spider):
    name = 'Navitime'
    allowed_domains = ['https://www.navitime.co.jp']
    start_urls = ['http://https://www.navitime.co.jp/']

    def parse(self, response):
        pass
