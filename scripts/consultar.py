from datetime import time, datetime, date, timedelta
import time
import requests

def run():
    agora = datetime.now()
    #print(agora)
    dataCotacao = str(agora.month) + '-' + str(agora.day) + '-' + str(agora.year)
    print(dataCotacao)

    codigoMoeda = 'EUR'

    link = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda=@codigoMoeda,dataInicialCotacao=@dataInicialCotacao,dataFinalCotacao=@dataFinalCotacao)?@codigoMoeda=\'' + codigoMoeda + '\'&@dataInicialCotacao=\'' + dataCotacao + '\'&@dataFinalCotacao=\'' + dataCotacao + '\'&$format=json&$select=cotacaoCompra'
    print(link)

    requisicaoCotacao = requests.get(link)
    print(requisicaoCotacao)

    if str(requisicaoCotacao) == '<Response [200]>':
        cotacao = requisicaoCotacao.json()
        print(cotacao)

    elif str(requisicaoCotacao) == '<Response [400]>':
        print("Codigo Moeda invalido, por favor digite novamente")

    elif str(requisicaoCotacao) == '<Response [404]>':
        print("Codigo Moeda não encontrado, por favor tente outro CEP")

    valorCotacao = cotacao['value']
    print(valorCotacao)



