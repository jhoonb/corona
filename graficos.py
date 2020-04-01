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


def ms_line(y: dict, ms: dict,output: str = "html", 
color: str = "black", passo=1, print_values=False) -> Tuple[str, str]:

    filename = ""
    if color == "black":
        graf = pygal.Line(print_values=print_values,
        x_label_rotation=90, 
        style=DarkStyle(value_colors=('white',)))
        filename = "data/line_ms_escuro"
    else:
        graf = pygal.Line(print_values=print_values,
        interpolate='cubic',
        x_label_rotation=90)
        filename = "data/line_ms_claro"
    
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
def ms_bar(ms: dict, output: str = "html", color: str = "black", passo=1) -> Tuple[str, str]:
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
    graf.add('Suspeitos', [ms[i]['suspeito'] for i in ms.keys()][::passo])
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
    import corona 
    c = corona.Corona()
    c.load_ms()
    print('gerando gráficos...')
    dados = {
        'Notificados': 'notificado',
        'Suspeitos': 'suspeito',
        'Confirmados': 'confirmado',
        'Descartados': 'descartado',
        'Excluídos': 'excluido',
        'Óbitos': 'obito'
    }
    
    a, b = ms_line(dados, c.ms, output="png", color="black", passo=1)
    a, b = ms_line(dados, c.ms, output="png", color="white", passo=1)
    a, b = ms_line(dados, c.ms, output="svg", color="black", passo=1)
    a, b = ms_line(dados, c.ms, output="svg", color="white", passo=1)
    #[TODO] grafico de barra
    print('ok')