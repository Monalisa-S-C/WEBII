from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.fazer_login, name='login'),
  path('cadastro/', views.cadastro, name='cadastro'),
  path('logout/', views.fazer_logout, name='logout')
]