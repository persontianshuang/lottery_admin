from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^search/', views.search),
    url(r'^manage/', views.search),
]


