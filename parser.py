
import requests

from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrawlingDjango.settings")
 
import django
django.setup()
from crawled_data.models import BoardData 
def naver_search_list(): 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser') 
    data = {'title':soup.select('span.item_title'), 'lank':soup.select('span.item_num')}
    return data


if __name__=='__main__':
    blog_data_dict = naver_search_list()
    queryset = BoardData.objects.all()  
    for data in queryset:
        data.delete()
    for t,l in zip(blog_data_dict['title'],blog_data_dict['lank']):
       BoardData(title = t.text, lank = l.text).save() 
