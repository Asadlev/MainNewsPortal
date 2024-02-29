from django.forms import ModelForm, TextInput, Textarea
from .models import News
from django.core.exceptions import ValidationError


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = [
            'author',
            'title',
            'text',
            'category',
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title == text:
            raise ValidationError(
                'Новость не должен быть идентичным заголовки'
            )

        elif len(text) < 20:
            raise ValidationError(
                'Новость не может быть таким коротким'
            )

        elif title[0].islower():
            raise ValidationError(
                'Заголовок должен начинаться с заглавной буквы'
            )

        return cleaned_data

