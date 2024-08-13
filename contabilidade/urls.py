from django.urls import path
from contabilidade.views import homepage, contas

urlpatterns = [
    path('', homepage),
    path('contas/', contas),
]
