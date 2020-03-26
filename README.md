COVID-19: Coronavírus - Monitor (Mundo e Brasil)
==

Página web: [corona](https://jhoonb.github.io/corona/) 

Dados do [Mato Grosso do Sul: _ms.json_](https://github.com/jhoonb/corona/tree/master/data)
===

Este pequeno programa em _Python_ monitora via terminal os dados referentes ao Coronavírus (COVID-19), usando como fonte de dados a plataforma _Microsoft Bing_.

A cada verificação é atualizado o arquivo `index.html`, uma página estática HTML
que expoe os dados para [jhoonb.github.io/corona/](https://jhoonb.github.io/corona/)

Em cada iteração para checar os dados é avaliado se a taxa de letalidade aumentou
ou diminuiu, com essa variação se emite um sinal sonoro: _rate_up.wav_ se a
taxa subir e _rate_down.wav_ se a taxa diminuir.


Em desenvolvimento
===

- Dados dos estados do Brasil
- Gráfico do crescimento de infectados e mortos no Brasil.

Uso
===

Linha de comando:

- Apenas gera a página index.html
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
height="493" width="581">

Objeto:
===

```python
from corona import Corona

## classe
corona = Corona()

## métodos
# dados do bing
corona.load()
# gera index.html
corona.index()
# sinal sonoro se a taxa de latalidade mudou
corona.check_change()
# monitora via terminal 
corona.monitor()

# ou 
corona.run()

## atributos 
# Fonte de dado: Microsoft Bing
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
Biblioteca:
===

Necessário instalar a lib simple audio para o som de alarme emitido. [simpleaudio](https://pypi.org/project/simpleaudio/)

```bash
pip3 install simpleaudio
```


Fonte de dados
===

- Microsoft Bing: [bing-covid](https://bing.com/covid) 

- Novel Coronavirus (COVID-19) Cases, provided by: [JHU CSSE](https://github.com/CSSEGISandData/COVID-19)