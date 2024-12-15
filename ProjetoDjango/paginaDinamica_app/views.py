from django.shortcuts import render
from django.http import HttpResponse
from math import sqrt


def home(request):
    return HttpResponse("Olá, Seja bem vindo ao meu site!")


def index(request):
    return render(request, 'index.html')


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
