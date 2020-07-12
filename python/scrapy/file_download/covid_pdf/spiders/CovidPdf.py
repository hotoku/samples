import scrapy
import re


class CovidpdfSpider(scrapy.Spider):
    name = 'CovidPdf'
    allowed_domains = ['www.city.akiruno.tokyo.jp']
    start_urls = ['http://www.city.akiruno.tokyo.jp/0000010831.html']

    def parse(self, response):
        urls = [
            re.sub("^./", "http://www.city.akiruno.tokyo.jp/", s)
            for s in
            response.xpath("//li//a/@href").re(r".+pdf$")
        ]
        yield dict(file_urls=urls)
