# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeadlineItem(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
