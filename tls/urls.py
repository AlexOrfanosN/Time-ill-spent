from api.models import SeriesResource
from django.conf import settings  
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  
from series import urls as series_urls
from . import views

series_resource = SeriesResource()

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('series/', include(series_urls)),
    path('api/', include(series_resource.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
