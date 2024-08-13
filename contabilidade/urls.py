from django.urls import path
from contabilidade.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
]
