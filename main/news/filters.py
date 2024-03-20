from django_filters import FilterSet
from .models import News

'''
Создаем свой набор фильтров для модели Product.
FilterSet, Который мы наследуем,
должен чем-то напомнить знакомые вам Django дженерики
'''
class NewsFilter(FilterSet):
    class Meta:
        model = News

        fields = {
            'author': ['icontains'],
        }






