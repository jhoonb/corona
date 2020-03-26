"""
uso em teste
local
"""
import urllib.request
import time 
import sys 
import json


def ms():
    link = 'https://www.vs.saude.ms.gov.br/Geral/vigilancia-saude/vigilancia-epidemiologica/boletim-epidemiologico/covid-19/'
    try:
        with urllib.request.urlopen(link) as response:
            data = response.read().decode("utf-8")
    except:
        return False
    
    index = data.find("noticiaBox") + 10
    data = data[index:]
    index = data.find('href="') + 6
    data = data[index:]
    index = data.find('">')
    boletim_link = data[:index]
    link_atual = "https://www.vs.saude.ms.gov.br/boletim-coronavirus-covid-19-19/"

    print(boletim_link)

    return True if link_atual != boletim_link else False


def monitor():
    resp = ms()
    hora = time.asctime(time.localtime(time.time())).split(" ")[3]
    if resp:
        print("\tNOVO BOLETIM MS!", "\t - NOVO")
    else:
        print("Nota Informativa: ", "[Nenhuma]", hora, end="\r")


if __name__ == '__main__':

    while True:
        print("\tCOVID-19 - SECRETARIA DE ESTADO DE SAÚDE MS")
        monitor()
        # mudar tempo de cada request
        time.sleep(120)
