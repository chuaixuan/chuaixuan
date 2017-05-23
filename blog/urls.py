from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^shop_list/$', views.shop_list, name='shop_list'),
    url(r'^pay_list/$',views.pay_list, name='pay_list'),
    url(r'^payment_page/$',views.payment_page,name='payment_page')
]