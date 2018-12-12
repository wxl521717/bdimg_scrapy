# -*- coding: utf-8 -*-
import scrapy
import re
from imgspider.items import ImgspiderItem
import time

class BdimgSpider(scrapy.Spider):
    name = "bdimg"
    allowed_domains = ["image.baidu.com"]
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=宠物&pn='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        
        item = ImgspiderItem()
        html = response.body.decode('utf-8','ignore')

        img_urls = re.findall('"objURL":"(.*?)",', html, re.S)
        #print (img_urls)

        for link in img_urls:

            item['images'] = link            
            detail = link[-26:-4]

            if '/' in detail:

                detail_str = detail.replace('/','1')
                item['flag'] = detail_str
            else:
            
                item['flag'] = detail

            yield item

        if self.offset < 600:

            self.offset += 60
            yield scrapy.Request(self.url+str(self.offset),callback = self.parse)



