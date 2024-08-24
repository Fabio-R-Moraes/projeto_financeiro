from django import forms
from .models import Conta

class ContaModelForm(forms.ModelForm):
    ativo = forms.BooleanField(
        label = 'Status',
        help_text='Marcado significa que a conta estará ativa.'
    )
    nome = forms.CharField(
        label = 'Conta',
        required=True,
        min_length= 4,
        max_length=100,
        error_messages={
            'min_length':'O nome de uma conta precisa de no mínimo 4 caracteres',
            'max_length':'O nome da conta não pode ultrapassar 100 caracteres',
        },
        widget=forms.TextInput(
            attrs={'placeholder':'Nome da conta financeira'}
        )
    )
    descricao = forms.CharField(
        label = 'Descrição',
        required = False,
        max_length = 300,
        widget=forms.Textarea(
            attrs={'rows':"3", "cols":"70", "placeholder":"Uma breve descrição"}
        )
    )
    saldo = forms.DecimalField(
        label = 'Saldo em R$',
        required=False,
        max_digits=9,
        decimal_places=2,
        min_value=0,
        error_messages={
            'min_value':'O saldo não pode ser menor que zero',
        }
    )
    
    class Meta:
        model = Conta
        fields = [
            'ativo',
            'nome',
            'descricao',
            'saldo',
        ]
