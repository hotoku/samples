import scrapy


class NavitimeSpider(scrapy.Spider):
    name = 'Navitime'
    allowed_domains = ['www.navitime.co.jp']
    start_urls = ['http://www.navitime.co.jp/']

    def parse(self, response):
        pass
