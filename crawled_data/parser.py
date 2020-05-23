
from crawled_data.models import BoardData
import django
import requests

from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrawlingDjango.settings")

django.setup()


def naver_search_list_crawled():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    url = 'https://datalab.naver.com/keyword/realtimeList.naver'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas = {'title': soup.select(
        'span.item_title'), 'lank': soup.select('span.item_num')}
    queryset = BoardData.objects.all()
    for data in queryset:
        data.delete()
    for t, l in zip(datas['title'], datas['lank']):
        BoardData(title=t.text, lank=l.text).save()


# if __name__=='__main__':
#     blog_data_dict = naver_search_list_crawled()
#     queryset = BoardData.objects.all()
#     for data in queryset:
#         data.delete()
#     for t,l in zip(blog_data_dict['title'],blog_data_dict['lank']):
#        BoardData(title = t.text, lank = l.text).save()
