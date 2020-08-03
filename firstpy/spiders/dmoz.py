import scrapy
from lxml import etree
from firstpy.items import MovieItem
from bs4 import BeautifulSoup


class DmozSpider(scrapy.Spider):
    name = "zhihu"
    # allowed_domains = ["https://maoyan.com"]

    start_urls = [
        "https://maoyan.com/board/4"
    ]

    def parse(self, response):

        print(response.body)
        # with open('t', 'wb') as f:
        #     f.write(response.body)
        # html = etree.parse('G:/work2\project/firstpy/firstpy/spiders/t', etree.HTMLParser())
        # html = etree.HTML(response.body)
        # print(html)
        # s = html.xpath('//dd')
        # print(s)
        # for m in s:
        #     item = MovieItem()
        #     item['index'] = m.xpath('.//a[@class="image-link"]/@href')[0]
        #     item['picUrl'] = m.xpath('.//img[@class="board-img"]/@data-src')[0][:-16]
        #     item['title'] = m.xpath('.//p[@class="name"]/a/text()')[0].encode('ISO-8859-1').decode('utf-8').strip()
        #     item['star'] = m.xpath('.//p[@class="star"]/text()')[0].encode('ISO-8859-1').decode('utf-8').strip()
        #     item['releaseTime'] = m.xpath('.//p[@class="releasetime"]/text()')[0].encode('ISO-8859-1').decode('utf-8')
        #     item['score'] = m.xpath('.//i[@class="integer"]/text()')[0] + m.xpath('.//i[@class="fraction"]/text()')[0]
        #     yield item

        # soup = BeautifulSoup(response.body, "lxml")
        # print("BeautifulSoup")
        # so = soup.select('dd')
        # for ss in so:
        #     item = MovieItem()
        #     item['index'] = ss.select_one('i').text
        #     item['title'] = ss.select('p[class="name"] a')[0].text.strip()#.encode('ISO-8859-1').decode('utf-8').strip()
        #     item['star'] = ss.select('p[class="star"]')[0].text.strip()#.encode('ISO-8859-1').decode('utf-8').strip()
        #     item['releaseTime'] = ss.select('p[class="releasetime"]')[0].text.strip()#.encode('ISO-8859-1').decode('utf-8')
        #     item['score'] = ss.select('i[class="integer"]')[0].text + ss.select('i[class="fraction"]')[0].text
        #     item['picUrl'] = ss.select('img[class="board-img"]')[0].get('data-src')[:-16]
        #     item['detailUrl'] = ss.select('a[class="image-link"]')[0].get('href')
        #     yield item
        #
        # for i in range(0, 90, 10):
        #     i += 10
        #     if i <= 90:
        #         yield scrapy.Request(
        #             url='https://maoyan.com/board/4?offset='+str(i),
        #             callback=self.parse
        #         )
