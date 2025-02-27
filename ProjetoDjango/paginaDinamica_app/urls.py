from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('resultado/', views.resultado, name='resultado'),
    path('autor/', views.autor, name='autor'),
    path('api/', include(router.urls)),
    path('calculo/' , views.calcular_hipotenusa, name='calculo'),
    path('formulario/', views.formulario, name='formulario')
]