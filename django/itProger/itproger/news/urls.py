from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_index, name='news_index'),
]