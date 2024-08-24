from django.urls import path
from contabilidade.views import IndexView, CreateContaView, UpdateContaView, DeleteContaView

app_name = 'contabilidade'

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('novaconta/', CreateContaView.as_view(), name='nova_conta'),
    path('<int:pk>/alterar/', UpdateContaView.as_view(), name='alterar_conta'),
    path('<int:pk>/excluir/', DeleteContaView.as_view(), name='excluir_conta'),
]
