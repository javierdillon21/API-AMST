from django.contrib import admin
from django.urls import path, re_path 
from api import views

urlpatterns = [
path('admin/', admin.site.urls),
re_path(r'^api/sensores$', views.sensor_data_list), re_path(r'^api/sensores/(?P<pk>[0-9]+)$',
views.sensor_data_detail)
]

