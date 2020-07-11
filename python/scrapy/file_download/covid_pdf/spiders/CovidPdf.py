import scrapy


class CovidpdfSpider(scrapy.Spider):
    name = 'CovidPdf'
    allowed_domains = ['www.city.akiruno.tokyo.jp']
    start_urls = ['http://www.city.akiruno.tokyo.jp/']

    def parse(self, response):
        pass
