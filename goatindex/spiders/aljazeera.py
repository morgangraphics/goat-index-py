import scrapy


class QuotesSpider(scrapy.Spider):
    name = "aljazeera"

    def start_requests(self):
        urls = [
            '',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath('// *[ @class ="article-p-wrapper"]//*/text()'):

            yield {
                'text': quote.extract()
            }
        # page = response.url.split("/")[-2]
        # filename = 'aljazerra-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
