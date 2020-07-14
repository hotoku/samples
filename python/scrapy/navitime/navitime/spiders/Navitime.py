from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import logging
import re


def to_text(node):
    return "".join([n.get() for n in node.xpath("text()")]).strip()


class NavitimeSpider(CrawlSpider):
    name = 'Navitime'
    allowed_domains = ['www.navitime.co.jp']
    start_urls = ['http://www.navitime.co.jp/category/']

    rules = [
        Rule(
            # LinkExtractor(allow=r"^https://www.navitime.co.jp/category/[0-9]+/$"),
            LinkExtractor(allow=r"^https://www.navitime.co.jp/category/0213/$"),
            callback="parse_page")
    ]

    def parse_page(self, response):
        self.logger.info(f"parse_page: {response.url}")

        address_nodes = response.css("ul.address-list > li.address-list-item > a")
        rex = re.compile(r"(.+)[(（]([0-9０-９]+)[）)]")

        def parse_address_text(node):
            text = to_text(node)
            return rex.sub(r"\1", text), int(rex.sub(r"\2", text))

        def url_in_address(node):
            return node.xpath("@href").get()

        if address_nodes:
            for node in address_nodes:
                _, cnt = parse_address_text(node)
                url = url_in_address(node)
                if cnt <= 15 * 50:
                    yield response.follow(url, self.yield_poi)
                else:
                    yield response.follow(url, self.parse_page)
        else:
            yield from self.yield_poi(response)

    def yield_poi(self, response):
        self.logger.info(f"yield_poi: {response.url}")

        name_nodes = response.xpath("//dt[not(child::span)][contains(@class, 'spot-name')]")
        names = map(to_text, name_nodes)
        for n in names:
            yield {
                "url": response.url,
                "name": n
            }
        nx = response.xpath("//span[contains(@class, 'paging-icon')][contains(@class, 'next')]/parent::a/@href")
        if nx:
            url = nx.get()
            yield response.follow(url, self.yield_poi)
