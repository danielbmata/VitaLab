from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages import constants
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
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso. Por favor, escolha outro.')
            return redirect('/usuarios/cadastro') 
        
        if not senha == confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.error(request, 'A senha deve conter 7 ou mais caracteres.')
            return redirect('/usuarios/cadastro')
        
        
        try:
            user = User.objects.create_user(
                first_name = primeiro_nome,
                last_name = ultimo_nome,
                username = username,
                password = senha,
                email = email,
            )
            messages.success(request,'Usuário cadastrado com sucesso!')
            
        except:
            messages.error(request,'Erro interno do sistema, contate um administrador.')
            
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')
    
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha, )
        
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username ou senha inválidos.')
            return redirect("/usuarios/login")
        
        
        
        return HttpResponse(f'{senha} e {username}')
