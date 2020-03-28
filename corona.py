import sys
import time
import urllib.request
import datetime
import json
import os

import simpleaudio as sa
from typing import List, Dict, Tuple

from str_index import HTML_INDEX_PAGE
import graficos

__all__ = [
    'Corona'
]

# def str2date(ds: str) -> datetime.datetime:
#     #fmt =  '%m-%d-%Y'
#     fmt = '%d-%m-%Y'
#     return datetime.datetime.strptime(ds, fmt)


# def _date2str(dt: datetime.datetime) -> str:
#     return dt.strftime("%m-%d-%Y")


def f_data(link: str, country: str) -> Dict[str, List]:

    with urllib.request.urlopen(link) as response:
        data = response.read().decode("utf-8")
    """
    Province/State,Country/Region,Lat,Long,1/22/20, ... ,3/23/20
    0         1           2     3    4     5      n-2     n-1
    """
    data = [i.strip() for i in data.split("\n")]
    header = data[0].split(',')[5:]
    _line = [i for i in data[1:] if country in i][0].strip()
    serie = _line.split(",")[5:]
    return {'header': header, 'series': list(map(int, serie))}


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


class Corona:
    """
    corona = Corona()
    corona.run()
    # or
    corona.load()
    corona.monitor()
    corona.index()
    """

    def __init__(self) -> None:
        self._data = {}
        self.links = None
        # Dados do Microsoft Bing
        self.world_cases = 0
        self.world_deaths = 0
        self.world_recovered = 0
        self.world_death_rate = 0.0
        self.world_recovered_rate = 0.0
        # Dados do Microsoft Bing
        self.brazil_cases = 0
        self.brazil_deaths = 0
        self.brazil_recovered = 0
        self.brazil_death_rate = 0.0
        self.brazil_recovered_rate = 0.0
        
        # json config file
        self._links = self._load_links()

        # JHU CSSE data
        self.br = {}

        # cache aux data
        self._aux_death_rate = 0
        self._aux_death_rate_brazil = 0
        # Mato Grosso do Sul
        self.ms = {}


    def _load_links(self) -> None:
        """ load links.json config file 
        """
        with open('links.json', 'r') as f:
            data = json.load(f)
        self.links = data


    def _rates(self) -> None:
        """ Calculate death rate and recovered rate 
        """
        _calc = lambda x, y: round(((x * 100) / y), 2)
        
        # aux 
        self._aux_death_rate = self.world_death_rate 
        self._aux_death_rate_brazil = self.brazil_death_rate
            
        # BING
        self.world_death_rate = _calc(
            self.world_deaths, self.world_cases)

        self.brazil_death_rate = _calc(
            self.brazil_deaths, self.brazil_cases)

        self.world_recovered_rate = _calc(
            self.world_recovered, self.world_cases)
            
        self.brazil_recovered_rate = _calc(
            self.brazil_recovered, self.brazil_cases)


    def check_change(self) -> None:
        """play a sound alert
        rate_down.wav for down death rate
        rate_up.wav for up death rate 
        """        
        path = os.path.abspath(os.getcwd()) + "/sound/"
        
        def play_sound(music: str) -> None:
            wave_obj = sa.WaveObject.from_wave_file(music)
            play_obj = wave_obj.play()
            play_obj.wait_done()
        
        # se taxa de mortalidade mundo/brazil diminuiu 
        # emite som rate_down.wav, do contrario 
        # emite alerta rate_up.wav
        if self._aux_death_rate < self.world_death_rate or \
            self._aux_death_rate_brazil < self.brazil_death_rate:
                    music = path + "rate_up.wav"
        elif self._aux_death_rate == self.world_death_rate or \
            self._aux_death_rate_brazil == self.brazil_death_rate: 
            return
        else:
            music = path + "rate_down.wav" 
        play_sound(music)


    def _load_br(self) -> None:
        """
        data from JHU: csse_covid_19_daily_reports
        https://github.com/CSSEGISandData/COVID-19
        """
        br = 'Brazil'
        series_cases = f_data(self.links['confirmed_link'], br)
        series_deaths = f_data(self.links['deaths_link'], br)
        series_recovered = f_data(self.links['recovered_link'], br)

        self.br = {
            'data': series_cases['header'],
            'caso': series_cases['series'],
            'morte': series_deaths['series'],
            'recuperado': series_recovered['series'] 
        }


    def _load_ms(self) -> None:
        """ms data json - SECRETARIA DE ESTADO E DE SAÚDE MS
        """
        with urllib.request.urlopen(self.links['ms']) as response:
            json_data = response.read().decode("utf-8")
            self.ms = json.loads(json_data)


    def _load_bing(self) -> None:
        """Bing Microsoft load data from url api
        """
        with urllib.request.urlopen(self.links['bing']) as response:
            json_data = response.read().decode("utf-8")
            self._data = json.loads(json_data)

        self.world_cases = self._data['totalConfirmed']
        self.world_deaths = self._data['totalDeaths']
        self.world_recovered = self._data['totalRecovered']

        # find brazil
        brazil = [i for i in self._data['areas'] if i['id'] == 'brazil'][0]
        self.brazil_cases = brazil['totalConfirmed']
        self.brazil_deaths = brazil['totalDeaths']
        self.brazil_recovered = brazil['totalRecovered']


    def load_comp(self, coutries: List[str]):
        """
        EUA, Italia, China, Spanha, Alemanha,Reino Unido, Irã, Coreia do Sul,
        Brasil.

        """
        pass


    def load(self) -> None:
        """ load data from url api
        """
        # caso não consiga capturar os dados ou
        # fora do ar a url: não encerra 
        try: 
            self._load_bing()
            self._load_ms()
            self._rates()
        except:
            print("\n[BING]: Url fora do ar ou inacessivel")
            print("  -> aguardando próxima checagem\n")


    def index(self) -> None:
        """Create index.html file 
        """
        # k = data do ultimo boletim
        k = list(self.ms.keys())[-1]
        # dados do ultimo boletim dia k
        ms = self.ms[k]
        # taxa de letalidade MS
        tx = round((ms['obito'] * 100) / ms['notificado'], 2)
        
        # grafico 
        graf, tab = graficos.ms_line(self.ms, output="html", color="black")
        localtime = time.asctime(time.localtime(time.time()))

        index = HTML_INDEX_PAGE.format(
            self.world_cases, 
            self.world_deaths,
            self.world_recovered,
            self.world_death_rate,
            self.world_recovered_rate,
            self.brazil_cases,
            self.brazil_deaths,
            self.brazil_recovered,
            self.brazil_death_rate,
            self.brazil_recovered_rate,
            # ms
            ms['notificado'],
            ms['suspeito'],
            ms['confirmado'],
            ms['descartado'],
            ms['excluido'],
            ms['obito'],
            tx,
            # grafico e tabela
            graf,
            tab,
            localtime)

        with open('index.html', 'w') as file:
            file.write(index)


    def monitor(self) -> None:
        """Linux console monitor
        """
        if sys.platform != 'linux':
            return self._monitor_win()

        dtime = datetime.datetime.now()
        dtime = dtime.strftime('%d/%m/%Y %H:%M')
        print(
            f"\n  -------- {CR['cyan']}CORONAVIRUS COVID-19{CR['reset']} --------",
            f"\n {CR['bblue']}{'jhoonb.github.io/corona':^40}{CR['reset']}",
            f"\n {CR['bgrey']}  atualizado em: {dtime:^23}{CR['reset']}",
            f"\n\n {'NÚMEROS NO MUNDO':^40}",
            f"\n - {'CASOS:':.<15}{self.world_cases:.>15}",
            f"\n - {CR['red']}{'MORTES:':.<15}{self.world_deaths:.>15}{CR['reset']}",
            f"\n - {CR['green']}{'RECUPERADOS:':.<15}{self.world_recovered:.>15}{CR['reset']}",
            f"\n - {CR['red']}{'TAXA DE LETALIDADE:':.<10}{self.world_death_rate:.>10}%{CR['reset']}",
            f"\n - {CR['green']}{'TAXA DE RECUPERADOS:':.<10}{self.world_recovered_rate:.>9}%{CR['reset']}",
            f"\n\n {'NÚMEROS NO BRASIL (Bing)':^40}",
            f"\n - {'CASOS:':.<15}{self.brazil_cases:.>15}",
            f"\n - {CR['red']}{'MORTES:':.<15}{self.brazil_deaths:.>15}{CR['reset']}",
            f"\n - {CR['green']}{'RECUPERADOS:':.<15}{self.brazil_recovered:.>15}{CR['reset']}",
            f"\n - {CR['red']}{'TAXA DE LETALIDADE:':.<10}{self.brazil_death_rate:.>10}%{CR['reset']}",
            f"\n - {CR['green']}{'TAXA DE RECUPERADOS:':.<10}{self.brazil_recovered_rate:.>9}%{CR['reset']}")

    
    def _monitor_win(self) -> None:
        """Windows console monitor
        """
        dtime = datetime.datetime.now()
        dtime = dtime.strftime('%d/%m/%Y %H:%M')
        print(
            f"\n  -------- CORONAVIRUS COVID-19 --------",
            f"\n {'jhoonb.github.io/corona':^40}",
            f"\n   atualizado em: {dtime:^25}",
            f"\n\n {'NÚMEROS NO MUNDO':^40}",
            f"\n - {'CASOS:':.<15}{self.world_cases:.>15}",
            f"\n - {'MORTES:':.<15}{self.world_deaths:.>15}",
            f"\n - {'RECUPERADOS:':.<15}{self.world_recovered:.>15}",
            f"\n - {'TAXA DE LETALIDADE:':.<10}{self.world_death_rate:.>10}%",
            f"\n - {'TAXA DE RECUPERADOS:':.<10}{self.world_recovered_rate:.>9}%",
            f"\n\n {'NÚMEROS NO BRASIL (Bing)':^40}",
            f"\n - {'CASOS:':.<15}{self.brazil_cases:.>15}"
            f"\n - {'MORTES:':.<15}{self.brazil_deaths:.>15}",
            f"\n - {'RECUPERADOS:':.<15}{self.brazil_recovered:.>15}",
            f"\n - {'TAXA DE LETALIDADE:':.<10}{self.brazil_death_rate:.>10}%",
            f"\n - {'TAXA DE RECUPERADOS:':.<10}{self.brazil_recovered_rate:.>9}%")

    
    def run(self) -> None:
        """ run check_change(), load(), monitor() and index()
        """
        self.check_change()
        self.load()
        self.monitor()
        self.index()

"""
# execute one time

python3 corona.py 

or

# execute in loop, step time in seconds
# 3600 seconds = 1 hour

python3 corona.py monitor 3600

"""

if __name__ == '__main__':
    print("Press Control + Z to exit...")
    msg_monitor = f'{CR["yellow"]} MONITOR COVID-19: '
    corona = Corona()
    if len(sys.argv) == 3:
        if sys.argv[1] == 'monitor':
            cont_tempo = 0
            # seconds
            cont_max = int(sys.argv[2])
            while True:
                tmp = time.asctime(time.localtime(time.time()))
                print(f'{msg_monitor}{tmp}{CR["reset"]}', end='\r')
                if cont_tempo % cont_max == 0:
                    corona.run()
                    cont_tempo = 0

                time.sleep(10) # 10 segs
                cont_tempo += 10
    else:
        corona.run()
