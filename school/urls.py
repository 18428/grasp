from django.conf.urls import url
from school import views

urlpatterns = [
    url(r'^main/', views.main, name='main'),
    url(r'^getMenu/', views.getMenu),
    url(r'^xsgl/', views.xsgl),
    url(r'^yhgl/', views.yhgl),
]