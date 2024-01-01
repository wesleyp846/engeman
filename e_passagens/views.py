from django.shortcuts import render
from django.http import HttpResponse

def passagens(request):
    return HttpResponse('passagens')
