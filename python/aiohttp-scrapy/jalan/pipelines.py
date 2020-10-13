# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class JalanPipeline:
    def process_item(self, item, spider):
        path = item["dest"]
        with open(path, "w") as f:
            json.dump(item, f, ensure_ascii=False)
