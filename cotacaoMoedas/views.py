from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from datetime import time, datetime, date, timedelta
import time, requests
from .models import Moeda, Cotacao
from .forms import HomepageForm, Moeda, EForm
import sqlite3, logging

# Create your views here.
class Homepage(ListView):
    template_name = "homepage.html"
    context_object_name = 'moedas'
    model = Moeda
    agora = datetime.now()
    logging.info(agora)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('DropBoxMoeda')
        #print(context['query'])
        codigoMoeda = str(context['query'])
        context['codigoMoeda'] = codigoMoeda
        nomeMoeda = ''

        if codigoMoeda == 'AUD':
            nomeMoeda = 'Dólar australiano'
        elif codigoMoeda == 'CAD':
            nomeMoeda = 'Dólar canadense'
        elif codigoMoeda == 'CHF':
            nomeMoeda = 'Franco suíço'
        elif codigoMoeda == 'DKK':
            nomeMoeda = 'Coroa dinamarquesa'
        elif codigoMoeda == 'EUR':
            nomeMoeda = 'Euro'
        elif codigoMoeda == 'GBP':
            nomeMoeda = 'Libra esterlina'
        elif codigoMoeda == 'JPY':
            nomeMoeda = 'Iene'
        elif codigoMoeda == 'NOK':
            nomeMoeda= 'Coroa Norueguesa'
        elif codigoMoeda == 'SEK':
            nomeMoeda = 'Coroa Sueca'
        elif codigoMoeda == 'USD':
            nomeMoeda = 'Dólar dos Estados Unidos'

        #print(codigoMoeda, nomeMoeda)
        context['nomeMoeda'] = nomeMoeda
        #context['nomeMoeda'] = {'moedas': moedas}

        context['d'] = self.request.GET.get('date')
        #print(context['d'])
        
        data_cotacao = '01-01-1990'
        data_cotacao = str(context['d'])
        ano = data_cotacao[-4:]
        mes = data_cotacao[:2]
        dia = data_cotacao[3:5]
        #print(ano)
        #print(mes)
        #print(dia)

        agora = datetime.now()
        # print(agora)
        dataCotacao = str(mes) + '-' + str(dia) + '-' + str(ano)

        link = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda=@codigoMoeda,dataInicialCotacao=@dataInicialCotacao,dataFinalCotacao=@dataFinalCotacao)?@codigoMoeda=\'' + codigoMoeda + '\'&@dataInicialCotacao=\'' + dataCotacao + '\'&@dataFinalCotacao=\'' + dataCotacao + '\'&$format=json&$select=cotacaoCompra'
        #print(link)

        requisicaoCotacao = requests.get(link)
        #print(requisicaoCotacao)

        if str(requisicaoCotacao) == '<Response [200]>':
            cotacao = requisicaoCotacao.json()
            #print(cotacao)
            valorCotacao = cotacao['value']
            valorCotacaod = valorCotacao[0]
            #print(valorCotacaod.value)
            for key, value in valorCotacaod.items():
                print(key, ":", value)
                context['valorCotacao'] = value

        elif str(requisicaoCotacao) == '<Response [400]>':
            print("Codigo Moeda invalido, por favor digite novamente")

        elif str(requisicaoCotacao) == '<Response [404]>':
            print("Codigo Moeda não encontrado, por favor tente outro codigo")

        elif str(requisicaoCotacao) == '<Response [500]>':
            print("Data invalida, por favor tente outra data")

        dia0 = '30'
        dia1 = 30
        dia2 = 30
        dia3 = 30
        dia4 = 30
        dia5 = 30

        if dia.isdigit():
            dia0 = ''.join(dia)
            dia1 = int(dia0) - 1
            dia2 = int(dia0) - 2
            dia3 = int(dia0) - 3
            dia4 = int(dia0) - 4
            dia5 = int(dia0) - 5
        else:
            dia0 = '30'
            dia1 = 30
            dia2 = 30
            dia3 = 30
            dia4 = 30
            dia5 = 30

 
        value0 = 0
        value1 = 0
        value2 = 0
        value3 = 0
        value4 = 0
        value5 = 0

        labels = [dia5, dia4, dia3, dia2, dia1, dia0]
        values = [value5, value4, value3, value2, value1, value0]

        con = sqlite3.connect("/home/renzo/CambioMoedas/db.sqlite3")
        c = con.cursor()

        # Read data from database
        sql = "SELECT * FROM `cotacaoMoedas_cotacao`"
        c.execute(sql)

        # Fetch all rows
        rows = c.fetchall()

        # Print results
        for row in rows:
            if row[1] == codigoMoeda:
                #print(row)
                data = row[4]
                anob = data[:4]
                mesb = data[5:7]
                diab = int(data[8:10])

                if anob == ano:
                    if mesb == mes:
                        #print(diab)
                        #print(dia1)
                        #print(dia2)
                        #print(dia3)
                        #print(dia4)
                        #print(dia5)
                        if diab == dia1:
                            #print(row[3])
                            if row[3] is not None:
                                value1 = row[3]
                                print(value1)
                            else:
                                value1 = 0
                        if diab == dia2:
                            if row[3] is not None:
                                value2 = row[3]
                                print(value2)
                            else:
                                value2 = 0
                        if diab == dia3:
                            if row[3] is not None:
                                value3 = row[3]
                                print(value3)
                            else:
                                value3 = 0
                        if diab == dia4:
                            if row[3] is not None:
                                value4 = row[3]
                                print(value4)
                            else:
                                value4 = 0
                        if diab == dia5:
                            if row[3] is not None:
                                value5 = row[3]
                                print(value5)
                            else:
                                value5 = 0
                        values = [value5, value4, value3, value2, value1, value]

        con.close()

        context['labels'] = labels
        context['values'] = values

        return context

        valorCotacao = context
