from django.shortcuts import render
from .models import BoardData 
from .parser import naver_search_list_crawled
# Create your views here. 
def naver_search_list(request):
    naver_search_list_crawled()
    datas = BoardData.objects.all()
    return render(request, 'index.html', {'datas': datas})