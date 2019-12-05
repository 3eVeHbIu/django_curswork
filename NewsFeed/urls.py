from django.urls import path, include

from .views import index, registration, create_post, edit, by_theme, show_my_news

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('create/', create_post, name='create'),
    path('news_edit/<int:news_id>/', edit, name='edit'),
    path('by_theme/<int:theme_id>/', by_theme, name='by_theme'),
    path('user/<str:username>/', show_my_news, name='my_news')
]
