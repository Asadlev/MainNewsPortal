from django.shortcuts import render
from django.views.generic import ListView
from .models import News
# Create your views here.


class NewsListView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    ordering = '-id'


