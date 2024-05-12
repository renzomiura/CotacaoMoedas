
from cotacaoMoedas.views import Homepage
from django.urls import path
# from django.contrib import admin
from . import views

app_name = 'calculadora'

#urlpatterns = [
#    path('', Homepage.as_view(), name='homepage'),
#]

urlpatterns = [

    path('', views.greetings, name='calculadora'),
    path('calculation', views.calculation)
]