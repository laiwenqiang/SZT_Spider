# -*- coding: utf-8 -*-
import scrapy
import requests
from PIL import Image
import pytesseract


class InvoiceSpider(scrapy.Spider):
    name = 'InvoiceSpider'
    allowed_domains = ['shenzhentong.com']

    def start_requests(self):
        verification_url = 'https://www.shenzhentong.com/ajax/WaterMark.ashx'

        with open('verification.GIF', 'wb') as i:
            i.write(requests.get(verification_url, stream=True).content)

        im = Image.open('verification.GIF')

        im = im.convert('L')

        def initTable(threshold=140):
            table = []
            for i in range(256):
                if i < threshold:
                    table.append(0)
                else:
                    table.append(1)
            return table

        bininaryImage = im.point(initTable(), '1')

        # text = pytesseract.image_to_string(bininaryImage, lang='eng', config='-psm 7')
        text = pytesseract.image_to_string(im)


        print text


        pass

    def parse_verification_code(self):

        pass


    def parse_page(self, response):

        pass