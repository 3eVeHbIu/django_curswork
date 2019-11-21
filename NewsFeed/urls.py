from django.urls import path, include

from .views import index

urlpatterns = [
    path('news/', index),
    path('accounts/', include('django.contrib.auth.urls')),
]
