# from lxml import etree
#
#
# html = etree.parse('G:/work2\project/firstpy/firstpy/spiders/t', etree.HTMLParser())
# #result = html.xpath('//li[@class="zm-topic-cat-item"]/a/text()')
# result = html.xpath('//dd')
# print(len(result))
# for i in range(len(result)):
#     print(result[i].xpath('//i[contains(@class,"board-index")]/text()')[i])
#     print(result[i].xpath('//p[@class="star"]/text()')[i].encode('ISO-8859-1').decode('utf-8'))
#
# for re in result:
#     print(re.xpath('.//i[contains(@class,"board-index")]/text()'))
#     print(re.xpath('.//p[@class="star"]/text()')[0].encode('ISO-8859-1').decode('utf-8'))
