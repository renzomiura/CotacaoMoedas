from django.utils import timezone
import datetime
from django.db import models

# Create your models here.
LISTA_CODIGOSMOEDAS = (
    ('AUD','AUD'),
    ('CAD','CAD'),
    ('CHF','CHF'),
    ('DKK','DKK'),
    ('EUR','EUR'),
    ('GBP','GBP'),
    ('JPY','JPY'),
    ('NOK','NOK'),
    ('SEK','SEK'),
    ('USD','USD'),
)

LISTA_MOEDAS = (
    ('Dólar australiano','Dólar australiano'),
    ('Dólar canadense','Dólar canadense'),
    ('Franco suíço','Franco suíço'),
    ('Coroa dinamarquesa','Coroa dinamarquesa'),
    ('Euro','Euro'),
    ('Libra Esterlina','Libra Esterlina'),
    ('Iene','Iene'),
    ('Coroa norueguesa','Coroa norueguesa'),
    ('Coroa sueca','Coroa sueca'),
    ('Dólar dos Estados Unidos','Dólar dos Estados Unidos'),
)

# criar Tabela Moeda
class Moeda(models.Model):
    codigo = models.CharField(max_length=5, choices=LISTA_CODIGOSMOEDAS)
    nome = models.CharField(max_length=50, choices=LISTA_MOEDAS)

    def __str__(self):
        return self.codigo

#criar Tabela Cotacao
class Cotacao(models.Model):
    codigo = models.CharField(max_length=5, choices=LISTA_CODIGOSMOEDAS)
    nome = models.CharField(max_length=50, choices=LISTA_MOEDAS)
    valor = models.FloatField(default=0)
    dataCotacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.valor


class EModel(models.Model):
    date = models.DateField()

