from django.conf.urls import url
from school import views

urlpatterns = [
    url(r'^demo/', views.demo, name='demo'),
]