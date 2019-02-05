from django.conf.urls import url
from school import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^sign_in/', views.sign_in),
    url(r'^data_json_user/', views.data_json_user),
    url(r'^new_submit/', views.new_submit),
    url(r'^main/', views.main, name='main'),
    url(r'^getMenu/', views.getMenu),
    url(r'^xsgl/', views.xsgl),
    url(r'^yhgl/', views.yhgl),
]