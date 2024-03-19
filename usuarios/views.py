from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            return redirect('/usuario/cadastro')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso. Por favor, escolha outro.')
            return redirect('/usuarios/cadastro') 
        
        try:
            user = User.objects.create_user(
                first_name = primeiro_nome,
                last_name = ultimo_nome,
                username = username,
                password = senha,
                email = email,
                )
        except:
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')
