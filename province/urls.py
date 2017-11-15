from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^order_list/$', views.order_list, name='order_list'),
    url(r'^member_list/$', views.member_list, name='member_list'),
]