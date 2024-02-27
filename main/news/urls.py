from django.urls import path, include
from .views import NewsListView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
]