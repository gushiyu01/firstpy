# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 豆瓣top250 movie
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    index = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    releaseTime = scrapy.Field()
    score = scrapy.Field()
    picUrl = scrapy.Field()
    detailUrl = scrapy.Field()


# 诗词排行榜top2000 poem
class PoemItem(scrapy.Item):
    id = scrapy.Field()
    poemContent = scrapy.Field()
    poemTitle = scrapy.Field()
    poemAuthor = scrapy.Field()
    poemDynasty = scrapy.Field()
    poemPicUrl = scrapy.Field()
