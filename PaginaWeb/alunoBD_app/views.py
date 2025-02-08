from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

def listar_alunos(request):
  alunos = Aluno.objects.all()
  return render(request, 'listar_alunos.html', {'alunos': alunos})



def criar_aluno(request):
  if request.method == "POST":
      form = AlunoForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('listar_alunos')
  else:
      form = AlunoForm()
  return render(request, 'criar_aluno.html', {'form': form})



def buscar_aluno(request):
  query = request.GET.get('q')
  resultados = Aluno.objects.filter(nome__icontains=query) if query else []
  return render(request, 'buscar_aluno.html', {'resultados': resultados, 'query': query})



def editar_aluno(request, aluno_id):
  aluno = get_object_or_404(Aluno, id=aluno_id)
  if request.method == "POST":
      form = AlunoForm(request.POST, instance=aluno)
      if form.is_valid():
          form.save()
          return redirect('listar_alunos')
  else:
      form = AlunoForm(instance=aluno)
  return render(request, 'editar_aluno.html', {'form': form})



def deletar_aluno(request, aluno_id):
  aluno = get_object_or_404(Aluno, id=aluno_id)
  if request.method == "POST":
      aluno.delete()
      return redirect('listar_alunos')
  return render(request, 'deletar_aluno.html', {'aluno': aluno})
