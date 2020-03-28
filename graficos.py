'''
Graficos em svg para o MS
'''
import pygal
from pygal.style import DarkStyle


class Graficos:

    def __init__(self, ms=None):
        self.ms = ms

    def linha(self):
        linha = pygal.Line(x_label_rotation=40)
        linha.title = 'COVID-19 | Mato Grosso do Sul\n Fonte: jhoonb.github.io/corona'
        linha.x_labels = self.ms.keys()
        linha.add('Notificados', [self.ms[i]['notificado'] for i in self.ms.keys()])
        linha.add('Suspeitos', [self.ms[i]['suspeito'] for i in self.ms.keys()])
        linha.add('Confirmados', [self.ms[i]['confirmado'] for i in self.ms.keys()])
        linha.add('Descartados', [self.ms[i]['descartado'] for i in self.ms.keys()])
        linha.add('Excluídos', [self.ms[i]['excluido'] for i in self.ms.keys()])
        linha.add('Óbitos', [self.ms[i]['obito'] for i in self.ms.keys()])
        #linha.render_to_file('glinha.svg')
        return linha.render(is_unicode=True), linha.render_table(style=False)


    def linhadark(self):

        linha = pygal.Line(x_label_rotation=40, style=DarkStyle)
        linha.title = 'COVID-19 | Mato Grosso do Sul\n Fonte: jhoonb.github.io/corona'
        linha.x_labels = self.ms.keys()
        linha.add('Notificados', [self.ms[i]['notificado'] for i in self.ms.keys()])
        linha.add('Suspeitos', [self.ms[i]['suspeito'] for i in self.ms.keys()])
        linha.add('Confirmados', [self.ms[i]['confirmado'] for i in self.ms.keys()])
        linha.add('Descartados', [self.ms[i]['descartado'] for i in self.ms.keys()])
        linha.add('Excluídos', [self.ms[i]['excluido'] for i in self.ms.keys()])
        linha.add('Óbitos', [self.ms[i]['obito'] for i in self.ms.keys()])
        #linha.render_to_file('glinhadark.svg')
        #return linha.render_table(style=True)
        return linha.render(is_unicode=True), linha.render_table(style=False)