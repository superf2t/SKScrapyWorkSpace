# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 定义字段

    # 职位名
    positionName = scrapy.Field();
    # 职位详情连接
    positionLink = scrapy.Field();
    # 职位类别
    positionType = scrapy.Field();
    # 职位人数
    positionNumber  = scrapy.Field();
    # 职位地址
    positionLocation = scrapy.Field();
    # 发布时间
    positionTime = scrapy.Field();


