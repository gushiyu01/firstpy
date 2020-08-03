import scrapy
from firstpy.items import PoemItem
from bs4 import BeautifulSoup


class PoemSpider(scrapy.Spider):
    name = "poem"

    start_urls = [
        "http://www.shicimingju.com/shicimark/aiqingshi_1_0__0.html"
    ]

    def parse(self, response):

        soup = BeautifulSoup(response.body, 'lxml')
        ss = soup.select('div[class="card shici_card"]')
        print(ss[0].select('div'))
        print(len(ss[0].select('div')))
        #for s in ss:
        for i in range(0, len(ss), 2):
            s = ss[i]
            # print(s)
            # top 2000
            # item = PoemItem()
            # item['id'] = (s.select('span')[0].text.strip())
            # item['poemAuthor'] = (s.select('a')[0].text.strip())
            # item['poemTitle'] = (s.select('h3')[0].text.strip())
            # item['poemDynasty'] = (s.select('div[class="list_num_info"]')[0].text.split('[')[1].split(']')[0])
            # item['poemContent'] = (s.select('div[class="shici_content"]')[0].text.replace('展开全文', '').strip()
            #                         .replace(' ', '').replace('\n', '').replace('收起', ''))
            # item['poemPicUrl'] = ('' if(len(s.select('img')) == 0) else s.select('img')[0].get('src')[:-46])
            # yield item
            # 爱情诗
            item = PoemItem()
            item['id'] = (s.select('div[class="list_num_info"]')[0].text.strip().split('[')[0].replace(' ', '').replace('\n', ''))
            item['poemAuthor'] = (s.select('div[class="list_num_info"]')[0].text.strip().split(']')[1].replace(' ', '').replace('\n', ''))
            item['poemTitle'] = (s.select('h3')[0].text.strip())
            item['poemDynasty'] = (s.select('div[class="list_num_info"]')[0].text.split('[')[1].split(']')[0])
            item['poemContent'] = (s.select('div[class="shici_content"]')[0].text.replace('展开全文', '').strip()
                                    .replace(' ', '').replace('\n', '').replace('收起', ''))
            item['poemPicUrl'] = ('' if(len(s.select('img')) == 0) else s.select('img')[0].get('src')[:-46])
            # yield item

        # for i in range(1, 7, 1):
        #     i += 1
        #     if i <= 7:
        #         yield scrapy.Request(
        #             url='http://www.shicimingju.com/shicimark/aiqingshi_'+str(i)+'_0__0.html',
        #             callback=self.parse
        #         )
