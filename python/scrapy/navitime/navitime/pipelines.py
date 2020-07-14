import sys
import logging
from pymongo import MongoClient


class NavitimePipeline:
    def process_item(self, item, spider):
        return item


class CountPoiPipeline:
    def __init__(self):
        super(CountPoiPipeline, self).__init__()
        self.count = 0

    def __del__(self):
        logging.info(f"number of poi's = {self.count}")

    def process_item(self, item, spider):
        self.count += item["count"]
        logging.debug(f'{item["category_id"]}, {item["prefecture"]}, {item["count"]}, {self.count}')
        return item


class MongoPipeline:
    def open_spider(self, spider):
        self.client = MongoClient()
        self.db = self.client.navitime
        self.collection = self.db.items

    def close_spider(self, spider):
        logging.info("closing mongo")
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
