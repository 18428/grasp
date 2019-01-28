from django.conf.urls import url
from school import views

urlpatterns = [
    url(r'^main/', views.main, name='main'),
]