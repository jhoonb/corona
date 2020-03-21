import os
import sys
import time
import urllib.request
import datetime

from str_index import HTML_INDEX_PAGE


def _toint(n):
    n = n.replace(",", "")
    try:
        n = int(n)
    except:
        raise Exception("fail to convert str to int")
    return n


CR = {
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'reset': '\u001b[0m',
    'yellow': '\u001b[33m',
    'cyan': '\u001b[36m'
}


class CoronaData:

    def __init__(self):
        self.world_cases = 0
        self.world_deaths = 0
        self.brazil_cases = 0
        self.brazil_deaths = 0
        self.world_death_rate = 0.0
        self.brazil_death_rate = 0.0

    
    def _rates(self):
        wdr = (self.world_deaths * 100) / self.world_cases
        bdr = (self.brazil_deaths * 100) / self.brazil_cases
        self.world_death_rate = round(wdr, 2)
        self.brazil_death_rate = round(bdr, 2)


    def load(self):
        link = "https://www.worldometers.info/coronavirus/"
        with urllib.request.urlopen(link) as response:
            html = response.read().decode("utf-8")
        
        # get Coronavirus Cases
        index_begin = html.find('#aaa">') + 6   
        # cut html     
        html = html[index_begin:]
        index_end = html.find('</span>')
        world_cases = html[:index_end].strip()

        # cut html
        html = html[index_end:]
        # get Deaths Number
        index_begin = html.find('<span>') + 6
        # cut html     
        html = html[index_begin:]
        index_end = html.find('</span>')
        world_deaths = html[:index_end].strip()

        # get brazil 
        # cut html
        html = html[index_end:]
        index_end = html.find('Brazil') + 11
        # cut html
        html = html[index_end:]
        # get brazil cases
        index_begin = html.find('">') + 2
        # cut html
        html = html[index_begin:]
        index_end = html.find('</td>')
        brazil_cases = html[:index_end].strip()

        # cut html
        html = html[index_end:]
        index_begin = html.find('">') + 2
        html = html[index_begin:]
        index_begin = html.find('">') + 2
        html = html[index_begin:]
        index_end = html.find('</td>')
        brazil_deaths = html[:index_end].strip()

        self.world_cases = _toint(world_cases)
        self.world_deaths = _toint(world_deaths)
        self.brazil_cases = _toint(brazil_cases)
        self.brazil_deaths = _toint(brazil_deaths)
        # rate
        self._rates()


    def create_page_index(self):
        localtime = time.asctime(time.localtime(time.time()))
        index = HTML_INDEX_PAGE.format(
            self.world_death_rate,
            self.brazil_death_rate,
            self.world_cases,
            self.world_deaths, 
            self.brazil_cases,
            self.brazil_deaths,
            localtime)

        with open('index.html', 'w') as file:
            file.write(index)


    def monitor(self):
        print(f"""

-------- {CR['cyan']}CORONAVIRUS COVID-19{CR['reset']} --------
- Casos no mundo:              {CR['red']}{self.world_cases}{CR['reset']}
- Número de mortos no Mundo:   {CR['red']}{self.world_deaths}{CR['reset']}
- Casos no Brasil:             {CR['red']}{self.brazil_cases}{CR['reset']}
- Número de Mortos no Brasil:  {CR['red']}{self.brazil_deaths}{CR['reset']}

- Taxa de Mortalidade(Mundo):  {CR['red']}{self.world_death_rate}%{CR['reset']}
- Taxa de Mortalidade(Brasil): {CR['red']}{self.brazil_death_rate}%{CR['reset']}

""")


def _convert2date(ds):
    fmt =  '%m-%d-%Y'
    return datetime.datetime.strptime(ds, fmt)


def sort_csv_file():
    pass


def get_brazil_data():
    pass


"""
# execute one time
python3 corona.py 

or
# execute in loop, step time in seconds
# 3600 seconds = 1 hour
python3 corona.py monitor 3600

"""

if __name__ == '__main__':
    corona = CoronaData()
    if len(sys.argv) == 3:
        if sys.argv[1] == 'monitor':
            cont_tempo = 0
            # seconds
            cont_max = int(sys.argv[2])
            while True:
                tmp = time.asctime(time.localtime(time.time()))
                print("Press Control + Z to exit...", end="\r")
                print(f'{CR["yellow"]} MONITOR COVID-19: {tmp}{CR["reset"]}', end="\r")
                if cont_tempo % cont_max == 0:
                    corona.load()
                    corona.monitor()
                    corona.create_page_index()
                    cont_tempo = 0

                time.sleep(10) # 10 segs
                cont_tempo += 10
    else:
        corona.load()
        corona.monitor()
        corona.create_page_index()
