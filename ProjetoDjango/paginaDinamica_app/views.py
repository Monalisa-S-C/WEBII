from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from math import sqrt
from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer
from django.contrib.auth.decorators import login_required

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


def home(request):
   # if request.method == 'POST':
      #  name = request.POST.get('name')
      #  email = request.POST.get('email')
      #  serie = request.POST.get('serie')

       # aluno = Aluno.objects.create(name=name, email=email, serie=serie)


    return render(request, 'home.html')

@login_required
def index(request):
    username = request.session.get('username')

    contexto = {
        'username': username
    }

    print('Nome:', username)
    return render(request, 'index.html', contexto)


def autor(request):
    return render(request, 'autor.html')


def resultado(request):
    if request.method == 'POST':
        cat1 = float(request.POST.get('cat1',0))
        cat2 = float(request.POST.get('cat2',0))

        hipotenusa = sqrt(cat1**2 + cat2**2)

        enunciado = "Seu enunciado é: o quadrado da hipotenusa é igual à soma dos quadrados dos catetos."
        explicacao = "O teorema de Pitágoras é uma relação matemática entre as medidas dos lados de um triângulo retângulo. Esse teorema está sintetizado na frase: o quadrado da hipotenusa é igual à soma dos quadrados dos catetos."
        resposta = f"A hipotenusa é: {hipotenusa}"

        return render(request, 'resultado.html', {
            'enunciado': enunciado,
            'explicacao': explicacao,
            'resposta': resposta
        })
    return HttpResponse("Método não permitido", status=405)



def calcular_hipotenusa(request):
    if request.method == "GET":
        cat1 = request.GET.get("cat1")
        cat2 = request.GET.get("cat2")

        if cat1 and cat2:
            try:
                cat1 = float(cat1)
                cat2 = float(cat2)
                hipotenusa = sqrt(cat1**2 + cat2**2)
                return JsonResponse({"hipotenusa": round(hipotenusa, 2)})
            except (ValueError, TypeError):
                return JsonResponse({"error": "Valores inválidos"}, status=400)

        return render(request, "pitagoras.html")

    return JsonResponse({"error": "Método não permitido"}, status=405)

def formulario(request):
    return render(request, 'formulario.html')