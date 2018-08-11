# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from SZT_Spider.dbhelper import *


class SztSpiderPipeline(object):
    def __init__(self):
        self.db = TestDBHelper()

    def process_item(self, item, spider):
        self.db.testCreateDatebase()
        self.db.testCreateTable()
        self.db.testInsert(item)
        return item


