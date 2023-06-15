"""
URL configuration for djangoapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from api import views
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [ 
    path('admin/', admin.site.urls), 
    re_path(r'^api/sensores$', views.sensor_data_list),
    re_path(r'^api/sensores/(?P<pk>[0-9]+)$', views.sensor_data_detail), 
    re_path(r'^api/lecturas$', views.lectura_data_list), re_path(r'^api/lecturas$', views.lectura_data_list),
    re_path(r'^api/lecturas/(?P<pk>[0-9]+)$', views.lectura_data_detail), 
    re_path(r'^db/nuevo-jwt', TokenObtainPairView.as_view,name='token_obtai n_pair'),
    re_path(r'^auth-jwt-refresh/', TokenRefreshView.as_view,name='token_refresh'),
    re_path(r'^auth-jwt-verify/', TokenVerifyView.as_view,name='token_ve rify'),
]


