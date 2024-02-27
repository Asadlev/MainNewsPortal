from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    author = models.CharField(User, max_length=29)
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.category}'


class Category(models.Model):
    NEWS_CHOICES = (
        ('SPORTS', 'sports'),
        ('RELIGIONS', 'religions'),
    )
    name = models.CharField(max_length=29, choices=NEWS_CHOICES)

    def __str__(self):
        return self.name
