from django.conf.urls import url, include

from django.shortcuts import render

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^games/(?P<platform_slug>[\w-]+)/$', views.ProductList.as_view(), name='list_filter'),
    url(r'^games/(?P<platform_slug>[\w-]+)/(?P<category_slug>[\w-]+)$', views.ProductList.as_view(), name='list_filter'),
    url(r'^games/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail.as_view(), name='detail' ),
]
