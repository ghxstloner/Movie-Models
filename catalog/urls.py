from operator import index
from django.urls import path as url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index')
]