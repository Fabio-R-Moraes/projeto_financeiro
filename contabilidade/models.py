from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Status', default=True)

    class Meta:
        abstract=True

class Conta(Base):
    nome = models.CharField('Conta', max_length=100, error_messages='Dê um nome para a conta')
    descricao = models.TextField('Descrição', max_length=300,)
    saldo = models.DecimalField('Saldo em R$', max_digits=9, decimal_places=2, default=0.00, help_text='Saldo financeiro da conta em Reais(R$)')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
    
def conta_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(conta_pre_save, sender=Conta)
