from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date, timedelta

def passagens(request):
    #ano=2024
    #mes=2
    mes = int(request.session.get('mes'))
    ano = int(request.session.get('ano'))
    primeiro_dia = date(ano, mes, 1)
                   
    # Calcula o primeiro dia do próximo mês
    primeiro_dia_proximo_mes = date(ano + (mes // 12), (mes % 12) + 1, 1)

    # Calcula o último dia do mês atual
    ultimo_dia_mes_atual = primeiro_dia_proximo_mes - timedelta(days=1)

    # Gera uma sequência de números de 1 até o último dia do mês
    dias = list(range(1, ultimo_dia_mes_atual.day + 1))
    
    dias_pares = []
    dias_impares = []

    for dia in dias:
    # Verifica se o número é par
        if dia % 2 == 0:
            dias_pares.append(dia)
        else:
            dias_impares.append(dia)
    return render(request, 'passagem.html', {'primeiro': primeiro_dia, 'proximo': primeiro_dia_proximo_mes, 'ultimo_dia': ultimo_dia_mes_atual, 'lista': dias, 'dias_pares': dias_pares, 'dias_impares': dias_impares})

def cria_pas(request):
    return render(request, 'cria_pas.html')

def pega_mes(request):
    mes = request.POST.get('mes')
    ano = request.POST.get('ano')

        # Armazena os valores na sessão
    request.session['mes'] = mes
    request.session['ano'] = ano
    return redirect('passagens')