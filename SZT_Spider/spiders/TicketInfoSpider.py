# -*- coding: utf-8 -*-
import scrapy


class TicketinfospiderSpider(scrapy.Spider):
    name = 'TicketInfoSpider'
    allowed_domains = ['shenzhentong.com']
    start_urls = ['http://query.shenzhentong.com:8080/sztnet/qrycard.jsp']

    def parse(self, response):
        print response.text
        pass
