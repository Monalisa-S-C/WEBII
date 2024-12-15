from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('resultado/', views.resultado, name='resultado'),
    path('autor/', views.autor, name='autor'),
]