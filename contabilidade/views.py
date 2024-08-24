from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Conta
from django.urls import reverse_lazy
from .forms import ContaModelForm

class IndexView(ListView):
    models = Conta
    template_name = 'homepage.html'
    queryset = Conta.objects.all().order_by('nome')
    context_object_name = 'contas'

class CreateContaView(CreateView):
    model = Conta
    template_name = 'conta_nova.html'
    form_class = ContaModelForm
    success_url = reverse_lazy('contabilidade:nova_conta')

class UpdateContaView(UpdateView):
    model = Conta
    template_name = 'conta_nova.html'
    fields = [
        'ativo',
        'nome',
        'descricao',
        'saldo'
    ]
    success_url = reverse_lazy('contabilidade:homepage')

class DeleteContaView(DeleteView):
    model = Conta
    template_name = 'conta_del.html'
    success_url = reverse_lazy('contabilidade:homepage')
