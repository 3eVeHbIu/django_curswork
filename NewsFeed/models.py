from django.db import models
from django.core import validators


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


class News(models.Model):
    headline = models.CharField(max_length=32,
                                verbose_name='Заголовок новости',
                                help_text='Введите название новости',
                                validators=[validators.MinLengthValidator(5)],
                                error_messages={'min_length': 'Слишком короткое название'})
    description = models.TextField(verbose_name='Содержание новости')
    edit_date_time = models.DateTimeField(auto_now=True,
                                          verbose_name='Дата и время последней правки')
    # creator =
    # image =
    subjects = models.ManyToManyField(Themes,
                                      verbose_name='Тематики',
                                      help_text='Подберите тематики')

    class Meta():
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-edit_date_time']
        #unique_together = ('headline', 'description')
