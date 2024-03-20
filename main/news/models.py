from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime
from django.core.cache import cache


class News(models.Model):
    author = models.CharField(max_length=29, unique=False)
    title = models.CharField(max_length=29)
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.text[:25]}'

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его



class Category(models.Model):
    NEWS_CHOICES = (
        ('SPORTS', 'sports'),
        ('RELIGIONS', 'religions'),
    )
    name = models.CharField(max_length=29, choices=NEWS_CHOICES)

    def __str__(self):
        return self.name
