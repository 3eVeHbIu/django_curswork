from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('NewsFeed.urls')),
    # значение по умолчанию html_email_temlate_name=None, что бы отправлялось письмо нужно это изменить
    # необходимо прописать свой маршрут на контроллер PasswordResetView со своими значениями
    # path('accounts/')
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
