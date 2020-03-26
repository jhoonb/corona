"""
APENAS PARA TESTE LOCAL
"""
import os
import urllib.request
import time 
import sys 
import datetime

import beepy

beepy.beep(sound=1)

def mt():
    link = 'http://www.saude.mt.gov.br/informe/584'
    with urllib.request.urlopen(link) as response:
        data = response.read().decode("utf-8")
    tag = 'Nota Informativa'


def ms():
    #link anterior: https://www.vs.saude.ms.gov.br/coronavirus-covid-19-4/
    link = 'https://www.vs.saude.ms.gov.br/coronavirus-covid-19-5/'
    try:
        with urllib.request.urlopen(link) as response:
            data = response.read().decode("utf-8")
    except:
        return False
    pdf = 'https://www.vs.saude.ms.gov.br/wp-content/uploads/2020/03/BOLETIM-CORONAVIRUS-25-03-2020.pdf'
    with urllib.request.urlopen(pdf) as response:
        data = response.read().decode("utf-8")
        with open('BOLETIM-CORONAVIRUS-25-03-2020.pdf', 'w') as file:
            file.write(data)
        os.system("nvlc /home/jhoonb/proj/corona/scripts/alert.mp3")
    return True



def monitor():
    resp = ms()
    hora = time.asctime(time.localtime(time.time())).split(" ")[3]
    if resp:
        print("\tNOVO BOLETIM MS!", "\t - NOVO")
    else:
        print("Nota Informativa: ", "NÃO SAIU AINDA - ", hora, end="\r")


if __name__ == '__main__':

    while True:
        print("\tCOVID-19 - SECRETARIA DE ESTADO DE SAÚDE MS")
        monitor()
        time.sleep(120) # 60*5 = 300
