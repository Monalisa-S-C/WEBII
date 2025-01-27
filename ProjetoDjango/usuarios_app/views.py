from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout


def fazer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            messages.success(request, "Login realizado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Credenciais inválidas.")
            return redirect('login')
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'cadastro.html')



def fazer_logout(request):
    logout(request)
    request.session.flush()
    messages.success(request, "Você saiu da conta.")
    return redirect('login')

