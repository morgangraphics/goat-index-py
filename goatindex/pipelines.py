# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from PIL import Image
import imagehash
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class GoatindexImagePipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        '''
        Overrides the default Image Pipeline via
        https://docs.scrapy.org/en/latest/topics/media-pipeline.html#topics-media-pipeline-override
        :param item: Image Item
        :param info: i.e. <scrapy.pipelines.media.MediaPipeline.SpiderInfo object at 0x7ff298ba2390>
        :return: scrapy request
        '''
        return [scrapy.Request(x, meta={'image_name': item["image_name"]})
                for x in item.get('image_urls', [])]

    def file_path(self, request, response=None, info=None):
        '''
        Path to save the images
        TODO:
            1. Need to pull IMAGES_STORE from settings.py file
            2. Keep Native file extension where applicable
        :param request:
        :param response:
        :param info:
        :return: saved image path
        '''
        return 'full/{0}.jpg'.format(request.meta['image_name'])

    def item_completed(self, results, item, info):
        '''
        TODO:
            1. Take image and classify it with Microsoft Image Classifier
                https://docs.microsoft.com/en-us/azure/machine-learning/preview/scenario-image-classification-using-cntk
            2. Store Results in a Database
        :param results:
        :param item:
        :param info:
        :return:
        '''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


# class DuplicatesPipeline(ImagesPipeline):
#         '''
#         This is not stateful
#         '''
#
#     def __init__(self):
#         self.ids_seen = set()
#
#     def hash_image(self, item):
#         '''
#         Will need to hash the image on save, then check the to see if the hash exists
#         This is an attempt to reduce Duplicate images
#         process_item version below is not stateful
#         If it is a dupe, +1 on mentions
#
#         hash = imagehash.average_hash(Image.open('images/full/foo-0.jpg'))
#
#         :param item:
#         :return:
#         '''
#         pass
#
#     def process_item(self, item, spider):
#         if item['id'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['id'])
#             return item
