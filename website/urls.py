from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from .import views

app_name="website"
urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),

    url(r'apps/(?P<id>\d+)/$', views.show_apps, name='show_apps'),

    url(r'contact/', views.contact, name='contact'),
    url(r'about/', views.about, name='about'),
    url(r'blog/', views.blog, name='blog'),
    url(r'viewer/', views.viewer, name='viewer'),
     #search page
    url(r'search/', views.search, name='search'),
    url(r'article/(?P<id>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'about_me/', views.about_me, name='about_me'),
]