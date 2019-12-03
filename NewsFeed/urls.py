from django.urls import path, include

from .views import index, registration, create_post

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('create/', create_post, name='create')
]
