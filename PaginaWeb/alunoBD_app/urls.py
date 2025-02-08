from django.urls import path
from .views import listar_alunos, criar_aluno, buscar_aluno, editar_aluno, deletar_aluno

urlpatterns = [
    path('', listar_alunos, name='listar_alunos'),
    path('novo/', criar_aluno, name='criar_aluno'),
    path('buscar/', buscar_aluno, name='buscar_aluno'),
    path('editar/<int:aluno_id>/', editar_aluno, name='editar_aluno'),
    path('deletar/<int:aluno_id>/', deletar_aluno, name='deletar_aluno'),
]
