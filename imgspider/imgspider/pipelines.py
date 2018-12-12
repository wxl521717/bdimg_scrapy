# -*- coding: utf-8 -*-
import os
import urllib
import socket

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ImgspiderPipeline(object):


    def process_item(self, item, spider):
        socket.setdefaulttimeout(10)

        path = '/home/wl/python/spider_test/image/'

        if not os.path.exists(path):
            
            os.makedirs(path)
        else:

            urllib.urlretrieve(item['images'],path + item['flag']+'.jpg')



        return item
