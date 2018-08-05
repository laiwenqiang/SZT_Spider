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
        card_real_amt = '//td[@id="cardRealAmt"]'

        for val in response.xpath(card_real_amt + '/text()').extract():  # 数组
            print val

        for val in response.xpath(card_real_amt + '/../td[2]/text()').extract():
            print val

        for val in response.xpath(card_real_amt + '/../td[4]/text()').extract():
            print val
        pass
