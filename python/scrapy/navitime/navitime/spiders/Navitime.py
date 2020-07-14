from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import logging
import re


class NavitimeSpider(CrawlSpider):
    name = 'Navitime'
    allowed_domains = ['www.navitime.co.jp']
    start_urls = ['http://www.navitime.co.jp/category/']

    rules = [
        Rule(
            # LinkExtractor(allow=r"^https://www.navitime.co.jp/category/[0-9]+/$"),
            LinkExtractor(allow=r"^https://www.navitime.co.jp/category/0206/$"),
            callback="parse_page")
    ]

    def parse_page(self, response):
        address_nodes = response.css("ul.address-list > li.address-list-item > a")

        if len(address_nodes) > 0:
            yield from self.yield_poi(response)
        else:
            yield from self.yield_poi(response)

        # def parse_text(text):
        #     return rex.sub(r"\1", text), int(rex.sub(r"\2", text))
        # texts = [parse_text(n.get().strip()) for n in
        #          .xpath("text()")]

        # if len(texts) != 47:
        #     logging.warning(f"number of extracted prefectures is less than 47. {url} {len(texts)}")

        # for t in texts:
        #     yield {
        #         "category_id": category_id,
        #         "prefecture": t[0],
        #         "count": t[1]
        #     }

        # links = [n.get() for n in
        #          response.css("ul.address-list > li.address-list-item > a").xpath("@href")]
        # for l in links:
        #     yield response.follow(l, self.parse_pref)

    def yield_poi(self, response):
        def get_name(node):
            return "".join([n.get() for n in node.xpath("text()")]).strip()

        name_nodes = response.xpath("//dt[not(child::span)][contains(@class, 'spot-name')]")
        names = map(get_name, name_nodes)
        for n in names:
            yield {
                "name": n
            }
