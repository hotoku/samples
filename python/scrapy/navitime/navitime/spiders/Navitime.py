from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class NavitimeSpider(CrawlSpider):
    name = 'Navitime'
    allowed_domains = ['www.navitime.co.jp']
    start_urls = ['http://www.navitime.co.jp/category/']

    rules = (
        Rule(LinkExtractor(allow=r"^https://www.navitime.co.jp/category/[0-9]+/$"),
             callback="parse_category"),
        Rule(LinkExtractor(allow=r"^https://www.navitime.co.jp/category/[0-9]+/[0-9]+/$"),
             callback="parse_category")
    )

    def parse_category(self, response):
        pass
