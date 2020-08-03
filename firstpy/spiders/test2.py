# from bs4 import BeautifulSoup
#
#
# soup = BeautifulSoup(open("G:/work2\project/firstpy/firstpy/spiders/t", "r", encoding='utf-8').read(), "lxml")
# print(soup.select('dd'))
# # with open('p', 'wb') as f:
# #     f.write(soup.prettify('utf-8'))
# ss = soup.select('dd')
# for s in ss:
#     print(s.select('p[class="name"] a')[0].text.strip())
#     print(s.select('p[class="name"] a')[0].get('title').strip())
#     print(s.select('p[class="star"]')[0].text.strip())
#     print(s.select('p[class="releasetime"]')[0].text.strip())
#     print(s.select('a[class="image-link"]')[0].get('href'))
#     print(s.select('i[class="integer"]')[0].text + s.select('i[class="fraction"]')[0].text)
