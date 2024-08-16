from django.urls import path
from contabilidade.views import IndexView, CreateContaView
from . import views

app_name = 'contabilidade'

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('novaconta/', CreateContaView.as_view(), name='nova_conta'),
    #path('contas/', views.conta_view, name='nova_conta'),
    #path('contas/create/', views.conta_create, name='create_conta'),
]
