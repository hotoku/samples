import scrapy
from jalan.items import JalanItem
import re
import os


class PoicollectorSpider(scrapy.Spider):
    name = 'PoiCollector'
    allowed_domains = ['jalan.net']
    start_urls = [
        f"https://www.jalan.net/travel/{i:02d}0000/?screenId=OUW1701&influxKbn=0"
        for i in range(1, 48)
    ]
    datadir = "./data"

    def __init__(self):
        super(PoicollectorSpider, self).__init__()
        if not os.path.isdir(self.datadir):
            os.makedirs(self.datadir)

    def dest_path(self, key):
        dest = os.path.join(self.datadir, key)
        return dest

    def parse(self, response):
        xpath = '//div[@class="areaList"]//dl[@class="spotsLinks"]'
        dls = response.xpath(xpath)
        for dl in dls:
            txt = dl.xpath("dt/text()")[0].get()
            if txt.strip() != "おすすめ観光スポット":
                continue
            for dd in dl.xpath("dd"):
                url = dd.xpath("a/@href").get()
                key = re.sub(r"/kankou/(.+)/", r"\1", url)
                dest = self.dest_path(key)
                if not os.path.isfile(dest):
                    self.logger.info(f"visiting url={response.url}")
                    yield response.follow(dd.xpath("a/@href").get(), self.parse_poi)
                else:
                    self.logger.info(f"skip url={response.url}")

    def parse_poi(self, response):
        key = re.sub(r"https://www.jalan.net/kankou/(.+)/.*", r"\1", response.url)
        name = response.xpath('//h1[@class="basicTitle"]/text()')[0].get()
        xpath = '//div[@class="aboutArea"]/table[@class="basicInfoTable"]/tr[child::th/text()="所在地"]/td/text()'
        address = response.xpath(xpath).get()
        item = {}
        item["dest"] = self.dest_path(key)
        item["key"] = key
        item["name"] = name.strip()
        item["address"] = re.sub(r"\s+", " ", address.strip())
        yield item
