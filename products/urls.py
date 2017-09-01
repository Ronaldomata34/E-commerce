from django.conf.urls import url, include

from django.shortcuts import render

from . import views


urlpatterns = [
    url(r'^home/$', views.HomePage.as_view(), name='home'),
    url(r'^games/$', views.ProductList.as_view(), name='list'),
    url(r'^games/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail' ),
]
