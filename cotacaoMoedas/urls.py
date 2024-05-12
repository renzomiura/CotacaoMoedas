# url
# view
# template

from django.urls import path, include, reverse_lazy
from cotacaoMoedas import views
from cotacaoMoedas.views import Homepage
from django.contrib.auth import views as auth_view

app_name = 'cotacaoMoedas'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
]
