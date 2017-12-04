from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^manage/', views.search, name='manage'),
]


