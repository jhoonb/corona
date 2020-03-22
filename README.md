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
height="308" width="371">

Objeto:
===

```python
from corona import CoronaData

## classe
corona = CoronaData()

## métodos
# dados json do bing
corona.load()
# gera index.html
corona.index()
# monitora via terminal 
corona.monitor()

## atributos 
# número de mortos no mundo (int)
corona.world_deaths
# número de mortos no Brasil (int)
corona.brazil_deaths
# número casos no mundo (int)
corona.world_cases
# número de casos no Brazil (int)
corona.brazil_cases
# número de recuperados no mundo (int)
corona.world_recovered
# número de recuperados no Brasil (int)
corona.brazil_recovered 
# taxa de mortalidade no mundo (float)
corona.world_death_rate
# taxa de mortalidade no Brasil (float)
corona.brazil_death_rate
# taxa de recuperados no mundo (float)
corona.world_recovered_rate 
# taxa de recuperados no Brasil (float)
corona.brazil_recovered_rate


```


Fonte de dados
===

- Microsoft Bing: [bing-covid](https://bing.com/covid) 

- Modelo baseado da página index.html: [minimalist-portfolio](https://github.com/giotsere/minimalist-portfolio)

- Novel Coronavirus (COVID-19) Cases, provided by: [JHU CSSE](https://github.com/CSSEGISandData/COVID-19)