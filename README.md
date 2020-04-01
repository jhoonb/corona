COVID-19: Coronavírus - Monitor (Mundo, Brasil e Mato Grosso do Sul)
==

Página web: [corona](https://jhoonb.github.io/corona/) 


MS
===
Para dados do Mato Grosso do Sul, clique em: [_ms.json_](https://github.com/jhoonb/corona/tree/master/data) (na pasta _data/_)

Sobre 
===
Este pequeno programa em _Python_ monitora via terminal os dados referentes ao Coronavírus (COVID-19), usando como fonte de dados _Worldmeters_.

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
====

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

Objeto _Corona_:
===

```python
from corona import Corona

## classe
corona = Corona()
# carrega os dados
corona.load()
# gera index.html
corona.index()
# sinal sonoro se a taxa de latalidade mudou
corona.check_change()
# monitora via terminal 
corona.monitor()

# ou executa todas os métodos acima
corona.run()

```
Biblioteca:
===

- Necessário instalar a lib simple audio para o som de alarme emitido. [simpleaudio](https://pypi.org/project/simpleaudio/)
- Biblioteca para geração de gráficos: [pygal](http://www.pygal.org/)

```bash
pip3 install simpleaudio
```


Fonte de dados
===
- Scrap da página [Worldmeters](https://www.worldometers.info/coronavirus/)
- Novel Coronavirus (COVID-19) Cases, provided by: [JHU CSSE](https://github.com/CSSEGISandData/COVID-19)


- [update 31/03] bing bloqueou API - dados agora da worldometers.info