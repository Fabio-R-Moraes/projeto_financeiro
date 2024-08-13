from django.contrib import admin
from .models import Conta

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'saldo', 'criado', 'modificado', 'ativo')
