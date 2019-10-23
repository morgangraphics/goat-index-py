import scrapy
from goatindex.spider_utils import *

util = SpiderUtils()

class AljazeeraSpider(scrapy.Spider):
    name = "aljazeera"



    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text = response.xpath('// *[ @class ="article-p-wrapper"]//*/text()')
        blob = text.extract()

        #nlppl = util.pipeline(response)

        #print(nlppl)

        #print(blob)
        #yield st




        #for text in response:
            #yield { text: text }
            #print(text)



        # page = response.url.split("/")[-2]
        # filename = 'aljazerra-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
