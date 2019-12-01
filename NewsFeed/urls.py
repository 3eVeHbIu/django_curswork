from django.urls import path, include

from .views import index, registration

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
]
