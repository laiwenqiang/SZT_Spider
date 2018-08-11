# -*- coding: utf-8 -*-
import scrapy
from SZT_Spider.items import TicketInfoItem


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
        print response.text
        card_real_amt = '//td[@id="cardRealAmt"]'

        item = TicketInfoItem()

        # item['card_amt'] = response.xpath(card_real_amt + '/text()').extract()[0]  # 数组

        # item['card_no'] = response.xpath(card_real_amt + '/../td[2]/text()').extract()[0]

        # item['last_use_time'] = response.xpath(card_real_amt + '/../td[4]/text()').extract()[0]

        item['card_no'] = '698474623'
        item['card_amt'] = 100.01
        item['last_use_time'] = '2018-05-11 19:31:31'
        print item

        return item
