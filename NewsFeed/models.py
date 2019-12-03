from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from datetime import datetime
from os.path import splitext


class Themes(models.Model):
    name = models.CharField(max_length=32,
                            db_index=True,
                            verbose_name='Тематика',
                            primary_key=True)

    class Meta:
        verbose_name_plural = 'Тематики'
        verbose_name = 'Тематика'
        ordering = ['name']

    def __str__(self):
        return self.name


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


class News(models.Model):
    headline = models.CharField(max_length=64,
                                verbose_name='Заголовок новости',
                                help_text='Введите название новости',
                                validators=[validators.MinLengthValidator(5)],
                                error_messages={'min_length': 'Слишком короткое название'})
    description = models.TextField(verbose_name='Содержание новости')
    edit_date_time = models.DateTimeField(auto_now=True,
                                          verbose_name='Дата и время последней правки')
    creator = models.ForeignKey(User,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE,
                                verbose_name='Автор')
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=get_timestamp_path,
                              blank=True,
                              null=True)
    subjects = models.ManyToManyField(Themes,
                                      verbose_name='Тематики',
                                      help_text='Подберите тематики')

    class Meta():
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-edit_date_time']
        #unique_together = ('headline', 'description')
