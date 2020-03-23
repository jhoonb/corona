"""
APENAS PARA TESTE LOCAL
"""
import urllib.request
import time 
import sys 
import datetime


def mt():
    link = 'http://www.saude.mt.gov.br/informe/584'
    with urllib.request.urlopen(link) as response:
        data = response.read().decode("utf-8")
    tag = 'Nota Informativa'


def ms():
    #link anterior: https://www.vs.saude.ms.gov.br/coronavirus-covid-19-3/
    link = 'https://www.vs.saude.ms.gov.br/coronavirus-covid-19-4/'
    try:
        with urllib.request.urlopen(link) as response:
            data = response.read().decode("utf-8")
    except:
        return False

    return True



def monitor():
    resp = ms()
    hora = time.asctime(time.localtime(time.time())).split(" ")[3]
    if resp:
        print("NOVO BOLETIM MS!", "\t - NOVO")
    else:
        print("Nota Informativa: ", "NÃO SAIU AINDA - ", hora, end="\r")


if __name__ == '__main__':

    while True:
        print("\tCOVID-19 - SECRETARIA DE ESTADO DE SAÚDE MS")
        monitor()
        time.sleep(1800)