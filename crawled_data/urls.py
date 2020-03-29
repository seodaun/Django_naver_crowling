from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.naver_search_list, name='naver_search_list'), 
]
