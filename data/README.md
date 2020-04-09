Dados do Estado do Mato Grosso do Sul
==

Arquivo contendo os dados monitorados pela Secretaria de Estado de Saúde 
do Mato Grosso do Sul

Gráfico atualizado até dia: 09-04-2020 (formato .PNG)
===

[claro]

<img src="https://raw.githubusercontent.com/jhoonb/corona/master/data/line_ms_claro.png" 
height="400" width="600">

[escuro]

<img src="https://raw.githubusercontent.com/jhoonb/corona/master/data/line_ms_escuro.png" 
height="400" width="600">


Apenas confirmados (a cada 2 dias) 
===

[claro]

<img src="https://raw.githubusercontent.com/jhoonb/corona/master/data/line_ms_confirmado_claro.png" height="400" width="600">

[escuro]

<img src="https://raw.githubusercontent.com/jhoonb/corona/master/data/line_ms_confirmado_escuro.png" 
height="400" width="600">


Fonte dos dados: [Boletim MS](https://www.vs.saude.ms.gov.br/Geral/vigilancia-saude/vigilancia-epidemiologica/boletim-epidemiologico/covid-19/)

JSON para consulta [_json_ (clique aqui)](https://github.com/jhoonb/corona/blob/master/data/ms.json)

API Url: `https://raw.githubusercontent.com/jhoonb/corona/master/data/ms.json`

exemplo:

```json

{
    "data": {
        "url": string,
        "notificado": number,
        "suspeito": number, 
        "confirmado": number,
        "descartado": number, 
        "excluido": number,
        "obito": number
    }
}
```


Código-Fonte: [corona](https://github.com/jhoonb/corona/)


Monitor do Coronavírus: [COVID-19 Monitor](https://jhoonb.github.io/corona)


Gráfico em formato .SVG (disponível no diretório)
