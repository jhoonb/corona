'''
Graficos em svg para o MS e BR
'''
import pygal
from pygal.style import DarkStyle, DefaultStyle
from typing import Tuple


__all__ = [
    'ms_line',
    'br_line'
]


def ms_line(y: dict, ms: dict, filename: str,
            output: str = "html", color: str = "black",
            passo=1, print_values=False) -> Tuple[str, str]:

    if not y:
        y = {
            'Notificados': 'notificado',
            'Em Investigação': 'investigacao',
            'Confirmados': 'confirmado',
            'Descartados': 'descartado',
            'Excluídos': 'excluido',
            'Óbitos': 'obito'
        }

    if color == "black":
        graf = pygal.Line(print_values=print_values,
                          x_label_rotation=90,
                          style=DarkStyle(value_colors=('white',)))
        filename = "data/line_ms_escuro" if not filename else "data/"+filename
    else:
        graf = pygal.Line(print_values=print_values,
                          interpolate='cubic',
                          x_label_rotation=90)
        filename = "data/line_ms_claro" if not filename else "data/"+filename

    graf.title = 'COVID-19 | Mato Grosso do Sul\n Fonte: jhoonb.github.io/corona'
    graf.x_labels = list(ms.keys())[::passo]
    for k, v in y.items():
        graf.add(k, [ms[i][v] for i in ms.keys()][::passo])

    if output == "html":
        return graf.render(is_unicode=True), graf.render_table(style=False)
    elif output == "svg":
        graf.render_to_file(filename=filename+".svg")
        return "", graf.render_table(style=False)
    else:
        graf.render_to_png(filename=filename+".png")
    return "", graf.render_table(style=False)

# [TODO]


def ms_bar(ms: dict = None, output: str = "html",
           color: str = "black", passo=1) -> Tuple[str, str]:
    filename = ""
    if color == "black":
        graf = pygal.Bar(print_values=True,
                         x_label_rotation=90,
                         style=DarkStyle(value_colors=('white',)))
        filename = "data/grafico_ms_escuro_bar"
    else:
        graf = pygal.Bar(print_values=True,
                         x_label_rotation=90)
        filename = "data/grafico_ms_claro_bar"

    graf.title = 'COVID-19 | Mato Grosso do Sul\n Fonte: jhoonb.github.io/corona'
    graf.x_labels = list(ms.keys())[::passo]
    graf.add('Notificados', [ms[i]['notificado'] for i in ms.keys()][::passo])
    graf.add('Em Investigação', [ms[i]['investigacao'] for i in ms.keys()][::passo])
    graf.add('Confirmados', [ms[i]['confirmado'] for i in ms.keys()][::passo])
    graf.add('Descartados', [ms[i]['descartado'] for i in ms.keys()][::passo])
    graf.add('Excluídos', [ms[i]['excluido'] for i in ms.keys()][::passo])
    graf.add('Óbitos', [ms[i]['obito'] for i in ms.keys()][::passo])
    if output == "html":
        return graf.render(is_unicode=True), graf.render_table(style=False)
    elif output == "svg":
        graf.render_to_file(filename=filename+".svg")
        return "", graf.render_table(style=False)
    else:
        graf.render_to_png(filename=filename+".png")
    return "", graf.render_table(style=False)


if __name__ == '__main__':
    import json
    with open('data/ms.json') as f:
        ms = json.loads(f.read())

    print('gerando gráficos...')
    dados = {
        'Notificados': 'notificado',
        'Em Investigação': 'investigacao',
        'Confirmados': 'confirmado',
        'Descartados': 'descartado',
        'Excluídos': 'excluido',
        'Óbitos': 'obito'
    }
    print_values = False
    passo = 7
    a, b = ms_line(dados, ms, None, output="png", color="black", passo=passo, print_values=print_values)
    a, b = ms_line(dados, ms, None, output="png", color="white", passo=passo, print_values=print_values)
    a, b = ms_line(dados, ms, None, output="svg", color="black", passo=passo, print_values=print_values)
    a, b = ms_line(dados, ms, None, output="svg", color="white", passo=passo, print_values=print_values)

    # confirmados
    dados = {'Confirmados': 'confirmado'}
    print_values = True
    passo = 7
    a, b = ms_line(
        dados, ms, filename="line_ms_confirmado_escuro", output="png",
        color="black", passo=passo, print_values=print_values)

    a, b = ms_line(
        dados, ms, filename="line_ms_confirmado_claro", output="png",
        color="white", passo=passo, print_values=print_values)

    a, b = ms_line(
        dados, ms, filename="line_ms_confirmado_escuro", output="svg",
        color="black", passo=passo, print_values=print_values)

    a, b = ms_line(
        dados, ms, filename="line_ms_confirmado_claro", output="svg",
        color="white", passo=passo, print_values=print_values)

    # obito
    dados = {'Óbito': 'obito'}
    print_values = True
    passo = 7
    a, b = ms_line(
        dados, ms, filename="line_ms_obito_escuro", output="png",
        color="black", passo=passo, print_values=print_values)

    a, b = ms_line(
        dados, ms, filename="line_ms_obito_claro", output="png",
        color="white", passo=passo, print_values=print_values)

    a, b = ms_line(
        dados, ms, filename="line_ms_obito_escuro", output="svg",
        color="black", passo=passo, print_values=print_values)

    a, b = ms_line(
        dados, ms, filename="line_ms_obito_claro", output="svg",
        color="white", passo=passo, print_values=print_values)
    # [TODO] grafico de barra
    print('ok')
