from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import mainPage

urlpatterns = [
    path('', mainPage, name='home'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
