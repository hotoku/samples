from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
import logging


class CountpoiSpider(CrawlSpider):
    name = 'CountPoi'
    allowed_domains = ['www.navitime.co.jp']
    start_urls = ['https://www.navitime.co.jp/category/']

    rules = [
        Rule(
            LinkExtractor(allow=r"^https://www.navitime.co.jp/category/[0-9]+/$"),
            # LinkExtractor(allow=r"^https://www.navitime.co.jp/category/0516/$"),
            callback="parse_category")
    ]

    def parse_category(self, response):
        url = response.url
        category_id = re.sub(r"^https://www.navitime.co.jp/category/([0-9]+)/$",
                             r"\1",
                             url)
        rex = re.compile(r"(.+)[(（]([0-9０-９]+)[）)]")

        def parse_text(text):
            return rex.sub(r"\1", text), int(rex.sub(r"\2", text))
        texts = [parse_text(n.get().strip()) for n in
                 response.css("ul.address-list > li.address-list-item > a").xpath("text()")]

        if len(texts) != 47:
            logging.warning(f"number of extracted prefectures is less than 47. {url} {len(texts)}")

        for t in texts:
            yield {
                "category_id": category_id,
                "prefecture": t[0],
                "count": t[1]
            }
