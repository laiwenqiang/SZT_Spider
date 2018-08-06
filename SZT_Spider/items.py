# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SztSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TicketInfoItem(scrapy.Item):
    card_no = scrapy.Field
    card_amt = scrapy.Field
    last_use_time = scrapy.Field
