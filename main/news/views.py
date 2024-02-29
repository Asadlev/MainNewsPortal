from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .forms import NewsForm
from .models import News
# Create your views here.


class NewsListView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    ordering = '-id'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'


class NewsCreateView(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'

