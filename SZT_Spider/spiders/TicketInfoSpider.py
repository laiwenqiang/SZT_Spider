# -*- coding: utf-8 -*-
import scrapy


class TicketinfospiderSpider(scrapy.Spider):
    name = 'TicketInfoSpider'
    allowed_domains = ['shenzhentong.com']

    def start_requests(self):
        url = 'http://query.shenzhentong.com:8080/sztnet/qryCard.do'

        yield scrapy.FormRequest(
            url=url,
            formdata={"cardno": "698474623"},  # TODO 目前cardno写死
            callback=self.parse_page
        )

    def parse_page(self, response):
        # print response.text
        for val in response.xpath('//td[@id="cardRealAmt"]/text()').extract():  # 数组
            print val
        pass
