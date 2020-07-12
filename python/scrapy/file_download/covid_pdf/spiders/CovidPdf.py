import scrapy


class CovidpdfSpider(scrapy.Spider):
    name = 'CovidPdf'
    allowed_domains = ['www.city.akiruno.tokyo.jp']
    start_urls = ['http://www.city.akiruno.tokyo.jp/0000010831.html']

    def parse(self, response):
        yield dict(file_urls=response.xpath("//li//a@href").re(r".+pdf$"))
