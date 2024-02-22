from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.series_main, name='series_main'),
    path('<int:series_id>', views.series_detail, name='series_detail')
]
