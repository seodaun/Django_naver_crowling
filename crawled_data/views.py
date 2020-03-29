from django.shortcuts import render
from .models import BoardData 
# Create your views here.
 
def naver_search_list(request):
    datas = BoardData.objects.all()
    return render(request, 'index.html', {'datas': datas})