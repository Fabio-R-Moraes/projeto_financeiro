from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'homepage.html')

def contas(request):
    return HttpResponse("Contas Financeiras...")
