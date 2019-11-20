from django.contrib import admin
from .models import News, Themes


class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'edit_date_time')
    list_display_link = ('headline',)
    search_fields = ('headline',)


admin.site.register(News, NewsAdmin)
admin.site.register(Themes)
