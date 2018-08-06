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

        print response.xpath(card_real_amt + '/text()').extract()[0]  # 数组

        print response.xpath(card_real_amt + '/../td[2]/text()').extract()[0]

        print response.xpath(card_real_amt + '/../td[4]/text()').extract()[0]

        pass
