import sys
import time
import urllib.request
import datetime
import pathlib
import json

from typing import List, Dict
from str_index import HTML_INDEX_PAGE


def _toint(n: str) -> int:
    n = n.replace(",", "")
    try:
        n = int(n)
    except:
        raise Exception("fail to convert str to int")
    return n


def _str2date(ds: str) -> datetime.datetime:
    fmt =  '%m-%d-%Y'
    return datetime.datetime.strptime(ds, fmt)


def _date2str(dt: datetime.datetime) -> str:
    return dt.strftime("%m-%d-%Y")


def csv_line(line: str) -> str:
    """
    format 
    key: [Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered,Latitude,Longitude]
             0,             1,                2,         3,      4,      5,        6,       7
    value:    ,     Brazil,     2020-03-17T15:33:06,    321,    1,     2,      -14.2350, -51.9253

    """
    confirmed, deaths = line.split(",")[3:5]
    confirmed = 0 if confirmed == '' else int(confirmed)
    deaths = 0 if deaths == '' else int(deaths)
    return confirmed, deaths


def brazil_data() -> List[Dict]:
    """
    data from JHU: csse_covid_19_daily_reports
    https://github.com/CSSEGISandData/COVID-19
    """

    _path_ = str(pathlib.Path().absolute() / 'data/')
    p = pathlib.Path(_path_)
    
    # utils functions
    rmcsv = lambda s: _str2date(s.split(".")[0])
    addcsv = lambda d: '{}/{}.csv'.format(_path_, _date2str(d))
    onlynename = lambda s: s.split("/")[-1].split(".")[0]
    
    # ordena por data
    files = sorted((rmcsv(i.name) for i in p.iterdir() if i.is_file()))
    files = [addcsv(i) for i in files]
    brazil_series = []
    for file in files:
        with open(file, 'r') as f:
            dados = [i.strip() for i in f.readlines() if 'Brazil' in i]
            if dados:
                confirmed, deaths = csv_line(dados[0])
                brazil_series.append(
                    {'date': onlynename(file),
                    'confirmed': confirmed,
                    'deaths': deaths 
                    })
        
    return brazil_series

# [test]
# def calc():

#     dados = brazil_data()
#     print(dados)
#     mortos = sum([i['deaths'] for i in dados])
#     casos = sum([i['confirmed'] for i in dados])
#     print(mortos)
#     print(casos)
    
#     line_chart = pygal.Line()
#     line_chart.title = 'Browser usage evolution (in %)'
#     line_chart.x_labels = map(str, range(2002, 2013))
#     line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
#     line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
#     line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
#     line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
#     x = line_chart.render(is_unicode=True) 
#     #line_chart.render_to_png("/home/jhoonb/proj/corona/opa.png")
#     with open('/home/jhoonb/proj/corona/opa.svg', 'w') as arq:
#         arq.write(x)


# console color [LINUX]
CR = {
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'reset': '\u001b[0m',
    'yellow': '\u001b[33m',
    'cyan': '\u001b[36m',
    'bblue': '\33[44m',
    'bgreen': '\33[42m',
    'bgrey': '\33[100m'
}


class CoronaData:

    def __init__(self):
        self._bingdata = None
        self.world_cases = 0
        self.world_deaths = 0
        self.world_recovered = 0
        self.brazil_cases = 0
        self.brazil_deaths = 0
        self.brazil_recovered = 0
        self.world_death_rate = 0.0
        self.brazil_death_rate = 0.0
        self.world_recovered_rate = 0.0
        self.brazil_recovered_rate = 0.0


    def _rates(self):

        _calc = lambda x, y: round(((x * 100) / y), 2)
        self.world_death_rate = _calc(self.world_deaths, self.world_cases)
        self.brazil_death_rate = _calc(self.brazil_deaths, self.brazil_cases)
        self.world_recovered_rate = _calc(self.world_recovered, self.world_cases)
        self.brazil_recovered_rate = _calc(self.brazil_recovered, self.brazil_cases)


    def load(self):
        # new source
        link = "https://www.bing.com/covid/data"
        with urllib.request.urlopen(link) as response:
            json_data = response.read().decode("utf-8")
            self._bingdata = json.loads(json_data)
        
        self.world_cases = self._bingdata['totalConfirmed']
        self.world_deaths = self._bingdata['totalDeaths']
        self.world_recovered = self._bingdata['totalRecovered']
        # find brazil
        for index, j in enumerate(self._bingdata['areas']):
            # [TODO] change 'brazil' for your country
            if j['id'] == 'brazil':
                self.brazil_cases = self._bingdata['areas'][index]['totalConfirmed']
                self.brazil_deaths = self._bingdata['areas'][index]['totalDeaths']
                self.brazil_recovered = self._bingdata['areas'][index]['totalRecovered']
                break
        # rate
        self._rates()


    def index(self):
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
        """
        Linux console monitor
        """
        if sys.platform != 'linux':
            return self._monitor_win()

        data_hora = datetime.datetime.now()
        data_hora = data_hora.strftime('%d/%m/%Y %H:%M')
        print(
            f"\n -------- {CR['cyan']}CORONAVIRUS COVID-19{CR['reset']} --------",
            f"\n{CR['bblue']}{'jhoonb.github.io/corona':^40}{CR['reset']}",
            f"\n{CR['bgrey']}atualizado em: {data_hora:^25}{CR['reset']}",
            f"\n{'NÚMEROS NO MUNDO':^40}",
            f"\n- {'CASOS:':<15}{CR['red']}{self.world_cases:>15}{CR['reset']}",
            f"\n- {'MORTES:':<15}{CR['red']}{self.world_deaths:>15}{CR['reset']}",
            f"\n- {'RECUPERADOS:':<15}{CR['green']}{self.world_recovered:>15}{CR['reset']}",
            f"\n{'NÚMEROS NO BRASIL':^40}",
            f"\n- {'CASOS:':<15}{CR['red']}{self.brazil_cases:>15}{CR['reset']}",
            f"\n- {'MORTES:':<15}{CR['red']}{self.brazil_deaths:>15}{CR['reset']}",
            f"\n- {'RECUPERADOS:':<15}{CR['green']}{self.brazil_recovered:>15}{CR['reset']}",
            f"\n{'TAXAS':^40}",
            f"\n- {'MORTALIDADE (Mundo):'}{CR['red']}{self.world_death_rate:>9}%{CR['reset']}",
            f"\n- {'MORTALIDADE (Brasil):'}{CR['red']}{self.brazil_death_rate:>8}%{CR['reset']}",
            f"\n- {'RECUPERADOS (Mundo):'}{CR['green']}{self.world_recovered_rate:>9}%{CR['reset']}",
            f"\n- {'RECUPERADOS (Brasil):'}{CR['green']}{self.brazil_recovered_rate:>8}%{CR['reset']}")

    
    def _monitor_win(self):
        """
        Windows console monitor
        """
        data_hora = datetime.datetime.now()
        data_hora = data_hora.strftime('%d/%m/%Y %H:%M')
        print(
            f"\n -------- CORONAVIRUS COVID-19 --------",
            f"\n{'jhoonb.github.io/corona':^40}",
            f"\natualizado em: {data_hora:^25}",
            f"\n{'NÚMEROS NO MUNDO':^40}",
            f"\n- {'CASOS:':<15}{self.world_cases:>15}",
            f"\n- {'MORTES:':<15}{self.world_deaths:>15}",
            f"\n- {'RECUPERADOS:':<15}{self.world_recovered:>15}",
            f"\n{'NÚMEROS NO BRASIL':^40}",
            f"\n- {'CASOS:':<15}{self.brazil_cases:>15}",
            f"\n- {'MORTES:':<15}{self.brazil_deaths:>15}",
            f"\n- {'RECUPERADOS:':<15}{self.brazil_recovered:>15}",
            f"\n{'TAXAS':^40}",
            f"\n- {'MORTALIDADE (Mundo):'}{self.world_death_rate:>9}%",
            f"\n- {'MORTALIDADE (Brasil):'}{self.brazil_death_rate:>8}%",
            f"\n- {'RECUPERADOS (Mundo):'}{self.world_recovered_rate:>9}%",
            f"\n- {'RECUPERADOS (Brasil):'}{self.brazil_recovered_rate:>8}%")



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
                    corona.index()
                    cont_tempo = 0

                time.sleep(10) # 10 segs
                cont_tempo += 10
    else:
        corona.load()
        corona.monitor()
        corona.index()
