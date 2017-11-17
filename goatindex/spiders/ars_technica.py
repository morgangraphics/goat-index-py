# -*- coding: utf-8 -*-
import scrapy


class ArsTechnicaSpider(scrapy.Spider):
    name = 'ars-technica'
    #for url in urls:
    #    yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for quote in response.xpath('// *[ @class ="article-p-wrapper"]//*/text()'):
            yield {
                'text': quote.extract()
            }
