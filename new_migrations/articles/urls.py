from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles import views

urlpatterns = [
    url(r'^all/$', views.articles),
    url(r'^get/(?P<article_id>\d+)/$', views.article),
]
