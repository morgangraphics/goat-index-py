# -*- coding: utf-8 -*-
import scrapy
from goatindex.items import ImageItem


class ImageSpider(scrapy.Spider):
    # Spider Name
    name = 'images'

    def start_requests(self):
        '''
        This is the default pattern for Scrapy i.e. scrapy crawl images
        You would normally put a starting URL here to begin the scraping process
        Kept for testing purposes
        :yield: scrapy.Request passing url and callback function
        '''
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ')
        urls = [
            'https://i.redd.it/w5kz4683xexz.jpg',
            'https://i.redd.it/nlngctqpcwwz.jpg',
            'https://i.redd.it/s2s9pjxahkwz.jpg',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        '''
        This is the default pattern for scrapy i.e. scrapy crawl images
        This is also the fallback for scrapyrt
        ImageItem() images.py is equivalent to a data schema
        :param response:
        :yield image
        '''
        image = ImageItem()
        image['image_urls'] = [response.url]
        #image['image_name'] = response.request.meta['image_name']
        yield image





