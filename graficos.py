'''
Graficos em svg para o MS e BR
'''
import pygal
from pygal.style import DarkStyle
from typing import Tuple


__all__ = [
    'ms_line',
    'br_line'
]


def ms_line(ms: dict, output: str = "html", color: str = "black") -> Tuple[str, str]:
    if color == "black":
        graf = pygal.Line(x_label_rotation=40, style=DarkStyle)
    else:
        graf = pygal.Line(x_label_rotation=40)
    graf.title = 'COVID-19 | Mato Grosso do Sul\n Fonte: jhoonb.github.io/corona'
    graf.x_labels = ms.keys()
    graf.add('Notificados', [ms[i]['notificado'] for i in ms.keys()])
    graf.add('Suspeitos', [ms[i]['suspeito'] for i in ms.keys()])
    graf.add('Confirmados', [ms[i]['confirmado'] for i in ms.keys()])
    graf.add('Descartados', [ms[i]['descartado'] for i in ms.keys()])
    graf.add('Excluídos', [ms[i]['excluido'] for i in ms.keys()])
    graf.add('Óbitos', [ms[i]['obito'] for i in ms.keys()])
    if output == "html":
        return graf.render(is_unicode=True), graf.render_table(style=False)
    elif output == "svg":
        graf.render_to_file(filename="grafico_ms.svg")
        return "", graf.render_table(style=False)
    else:
        graf.render_to_png(filename="grafico_ms.png")
    return "", graf.render_table(style=False)


def br_line(br: dict, output: str = "html", color: str = "black") -> Tuple[str, str]:
    if color == "black":
        graf = pygal.Line(x_label_rotation=90, style=DarkStyle)
    else:
        graf = pygal.Line(x_label_rotation=90)
    graf.title = 'COVID-19 | Brasil\n Fonte: jhoonb.github.io/corona'
    # gráfico a cada três dias
    graf.x_labels = br['data'][::3]
    graf.add('Casos', br['caso'][::3])
    graf.add('Mortes', br['morte'][::3])
    graf.add('Recuperados', br['recuperado'][::3])
    if output == "html":
        return graf.render(is_unicode=True), graf.render_table(style=False)
    elif output == "svg":
        graf.render_to_file(filename="grafico_br.svg")
        return "", graf.render_table(style=False)
    else:
        graf.render_to_png(filename="grafico_br.png")
    return "", graf.render_table(style=False)