from django.urls import path, include
from .views import NewsListView, NewsDetailView, NewsCreateView


app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/detail', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='create'),
]