COVID-19: Death Rate - (Taxa de Mortalidade do Coronavírus)
==

Página web: [corona](https://jhoonb.github.io/corona/) 
===

Uso
===

Linha de comando:

- Gera a página index.html
```bash
python3 corona.py
```

- Monitor do COVID-19 no terminal
- Faz consulta a cada `<numero>` segundos e gera a página `index.html`
```bash
python3 corona.py monitor <numero>
```
- exemplo, a cada 2 minutos (120 segundos):
```bash
python3 corona.py monitor 120
```
(para sair pressione `Control + Z`)


Imagem do terminal executando o monitor:

<img src="https://raw.githubusercontent.com/jhoonb/corona/master/example-terminal.png" 
height="468" width="599">

Objeto:
===

```python
from corona import Corona

## classe
corona = Corona()

## métodos
# dados json do bing
corona.load()
# gera index.html
corona.index()
# monitora via terminal 
corona.monitor()

## atributos 
# duas fontes de dados: Microsoft Bing e G1 Globo
# número de mortos no mundo (dict) {'bing': int, 'g1': int}
corona.world_deaths
# número de mortos no Brasil (dict) {'bing': int, 'g1': int}
corona.brazil_deaths
# número casos no mundo (dict) {'bing': int, 'g1': int}
corona.world_cases
# número de casos no Brazil (dict) {'bing': int, 'g1': int}
corona.brazil_cases
# número de recuperados no mundo (dict) {'bing': int, 'g1': int}
corona.world_recovered
# número de recuperados no Brasil (dict) {'bing': int, 'g1': int}
corona.brazil_recovered 
# taxa de mortalidade no mundo (dict) {'bing': int, 'g1': float}
corona.world_death_rate
# taxa de mortalidade no Brasil (dict) {'bing': int, 'g1': float}
corona.brazil_death_rate
# taxa de recuperados no mundo (dict) {'bing': int, 'g1': float}
corona.world_recovered_rate 
# taxa de recuperados no Brasil (dict) {'bing': int, 'g1': float}
corona.brazil_recovered_rate

# exemplo. número de casos confirmados (fonte bing)
corona.world_cases['bing']

# exemplo. número de casos confirmados (fonte bing)
corona.brazil_cases['g1']
```


Fonte de dados
===

- Microsoft Bing: [bing-covid](https://bing.com/covid) 

- G1 Globo (APENAS DADOS DO BRASIL): [G1](https://especiais.g1.globo.com/bemestar/coronavirus/mapa-coronavirus/)

- Novel Coronavirus (COVID-19) Cases, provided by: [JHU CSSE](https://github.com/CSSEGISandData/COVID-19)