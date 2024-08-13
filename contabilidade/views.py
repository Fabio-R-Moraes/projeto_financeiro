from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Conta

class IndexView(ListView):
    models = Conta
    template_name = 'homepage.html'
    queryset = Conta.objects.all()
    context_object_name = 'contas'
