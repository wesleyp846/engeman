from django.shortcuts import render, redirect
from django.http import HttpResponse
from hashlib import sha256
from .models import Funcionario  

def login(request):
    return  render(request, 'login.html')

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('cria_pas')
    status = request.GET.get('status')
    return render(request, 'cadastro.html',  {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    usuario = Funcionario.objects.filter(nome=nome)
    print('Prints de debug')
    print(usuario)
    if len(nome.strip()) == 0 or len(senha.strip()) == 0:
        return redirect ('/cadastro/?status=1')
    
    if len(senha) < 6:
        return redirect ('/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect ('/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Funcionario(nome=nome, senha=senha)
        usuario.save()
        return redirect ('/cadastro/?status=0')
    except:
        return redirect('/cadastro/?status=4')

def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    print('Print de debug')
    print(nome)
    print(senha)

    senha= sha256(senha.encode()).hexdigest()

    funcionario = Funcionario.objects.filter(nome=nome).filter(senha=senha)

    if len(funcionario) == 0:
        return HttpResponse('Não existe esse funcionario')
        #return redirect('/auth/login/?status=1')

    elif len(funcionario) > 0:
        request.session['funcionario'] = funcionario[0].id
        return redirect(f'/cria_pas/')

    return HttpResponse(f'{nome}  --- {senha}')