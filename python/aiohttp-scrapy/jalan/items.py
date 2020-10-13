# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JalanItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    key = scrapy.Field()

    pass
