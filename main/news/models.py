from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime


class News(models.Model):
    author = models.CharField(max_length=29, unique=True)
    title = models.CharField(max_length=29)
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.text[:25]}'

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])


class Category(models.Model):
    NEWS_CHOICES = (
        ('SPORTS', 'sports'),
        ('RELIGIONS', 'religions'),
    )
    name = models.CharField(max_length=29, choices=NEWS_CHOICES)

    def __str__(self):
        return self.name
