from django.urls import path, include

from .views import index, registration, create_post, edit

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('create/', create_post, name='create'),
    path('news_edit/<int:news_id>/', edit, name='edit'),
]
