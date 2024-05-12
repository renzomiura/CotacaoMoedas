from datetime import time, datetime, date, timedelta
import time
import requests
from cotacaoMoedas.models import Cotacao
import sqlite3

def run():
    agora = datetime.now()
    #print(agora)
    dias = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    listaMoedas = ['AUD', 'CAD', 'CHF', 'DKK', 'EUR', 'GBP', 'JPY', 'NOK', 'SEK', 'USD']
    vlrCotacao = 0

    for codigoMoeda in listaMoedas:

        if codigoMoeda == 'AUD':
            nomeMoeda = 'Dólar Australiano'
        elif codigoMoeda == 'CAD':
            nomeMoeda = 'Dólar Canadense'
        elif codigoMoeda == 'CHF':
            nomeMoeda = 'Franco Suíço'
        elif codigoMoeda == 'DKK':
            nomeMoeda = 'Coroa Dinamarquesa'
        elif codigoMoeda == 'EUR':
            nomeMoeda = 'Euro'
        elif codigoMoeda == 'GBP':
            nomeMoeda = 'Libra Esterlina'
        elif codigoMoeda == 'JPY':
            nomeMoeda = 'Iene'
        elif codigoMoeda == 'NOK':
            nomeMoeda = 'Coroa Norueguesa'
        elif codigoMoeda == 'SEK':
            nomeMoeda = 'Coroa Sueca'
        elif codigoMoeda == 'USD':
            nomeMoeda = 'Dólar Americano'

        for mes in meses:
            for dia in dias:
                dataCotacao = str(mes) + '-' + str(dia) + '-' + str('2022')
                #print(dataCotacao)
                dataBD =  str('2022') + '-' + str(mes) + '-' + str(dia) + ' ' + str('12') + str(':') + str('00') # + str('00') + str('127325') # + tzinfo=pytz.UTC


                link = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda=@codigoMoeda,dataInicialCotacao=@dataInicialCotacao,dataFinalCotacao=@dataFinalCotacao)?@codigoMoeda=\'' + codigoMoeda + '\'&@dataInicialCotacao=\'' + dataCotacao + '\'&@dataFinalCotacao=\'' + dataCotacao + '\'&$format=json&$select=cotacaoCompra'
                #print(link)

                time.sleep(10)
                requisicaoCotacao = requests.get(link)
                print(requisicaoCotacao)

                if str(requisicaoCotacao) == '<Response [200]>':
                    cotacao = requisicaoCotacao.json()
                    #print(cotacao)
                    vlCotacao = (cotacao['value'])
                    #print(vlCotacao)
                    # converter a lista em dicionario
                    for (index, d) in enumerate(vlCotacao):
                        dic = dict(d, index=index)
                        print(dic)
                        valorCotacao = dic['cotacaoCompra']
                        vlrCotacao = valorCotacao
                        print(vlrCotacao)

                    con = sqlite3.connect("db.sqlite3")
                    c = con.cursor()
                    maxID = c.execute('SELECT max(id) FROM cotacaoMoedas_cotacao')
                    print(maxID)
                    for row in maxID:
                        #print(row)
                        aID = row[0]
                        print(aID)
                        nID = aID + 1
                        print(nID)

                    #print(row[0])
                    # tid = Moeda(id=row[0])
                    # tcod = Moeda(codigo='EUR')
                    # tnome = Moeda(nome='Euro')
                    # tvalor = Moeda(valor=valorCotacao)
                    # tdata = Moeda(dataCotacao=dataCotacao)

                    trow = Cotacao(nID, codigoMoeda, nomeMoeda, vlrCotacao, dataBD)
                    trow.save()
                    c.close()

                elif str(requisicaoCotacao) == '<Response [400]>':
                    print("Codigo Moeda invalido, por favor digite novamente")

                elif str(requisicaoCotacao) == '<Response [404]>':
                    print("Codigo Moeda não encontrado, por favor tente outro Codigo")
    