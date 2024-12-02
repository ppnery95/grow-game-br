from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import random

class FirstWindow(Screen):
    pass

class Instrucoes1Carta(Screen):
    pass

class Instrucoes2Cartas(Screen):
    pass

class Instrucoes3Cartas(Screen):
    pass

class OpcoesJogo(Screen):
    pass

class CartaValor1Carta(Screen):
    pass

class Copiar1Carta(Screen):
    pass

class CartaValor2Cartas(Screen):
    pass

class CartaDesafio2Cartas(Screen):
    pass

class Copiar2Cartas(Screen):
    pass

class CartaValor3Cartas(Screen):
    pass

class CartaDesafio3Cartas(Screen):
    pass

class CartaAcao3Cartas(Screen):
    pass

class Copiar3Cartas(Screen):
    pass

class WindowManager(ScreenManager):
    pass

copy_valor = ''
copy_desafio = ''
copy_acao = ''

def add_to_copy(card, comment, card_type):
    global copy_valor, copy_desafio, copy_acao
    if card_type == 'valor':
        copy_valor = f'Carta VALOR selecionada: {card} \n\nComentários: {comment}'
        print(copy_valor)

    if card_type == 'desafio':
        copy_desafio = f'Carta DESAFIO selecionada: {card} \n\nComentários: {comment}'
        print(copy_desafio)

    if card_type == 'acao':
        copy_acao = f'Carta AÇÃO selecionada: {card} \n\nComentários: {comment}'
        print(copy_acao)

def copy_to_clickboard(game_type):
    if game_type == '1 carta':
        print(copy_valor)
        Clipboard.copy(copy_valor)

    if game_type == '2 cartas':
        print(copy_desafio)
        Clipboard.copy(copy_valor + '\n\n\n' + copy_desafio)

    if game_type == '3 cartas':
        print(copy_acao)
        Clipboard.copy(copy_valor + '\n\n\n' + copy_desafio + '\n\n\n' + copy_acao)

class DrawButtonValor(Button):
    cards = ['Carta 1', 'Carta 2', 'Carta 3', 'Carta 4', 'Carta 5']
    cards_valores = [
        'EQUIDADE \nDE GÊNERO',
        'INCLUSÃO',
        'DIVERSIDADE',
        'DEMOCRACIA',
        'DIGNIDADE',
        'CRIATIVIDADE \n(LIBERDADE DE \nEXPRESSÃO)',
        'IMPESSOALIDADE',
        'COOPERAÇÃO / \nCOMPARTILHAMENTO',
        'INOVAÇÃO',
        'LIBERDADE',
        'PARTICIPAÇÃO \nSOCIAL',
        'ACESSIBILIDADE',
        'COMPROMETIMENTO',
    ]    

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.text = 'Retira\n carta'
        self.bind(on_press=self.button_click)

    def button_click(self, instance):
        card = random.choice(self.cards_valores)
        self.text = card

class DrawButtonDesafio(Button):
    cards = ['Carta 1', 'Carta 2', 'Carta 3', 'Carta 4', 'Carta 5']
    cards_desafios = [
        'SEXISMO',
        'COLONIALISMO',
        'RACISMO',
        'POLÍTICAS \nALIMENTARES',
        'DESLOCAMENTO',
        'POLUIÇÃO',
        'CRIME',
        'DESIGUALDADE \nSOCIAL',
        'VÍCIO',
        'DOENÇA',
    ]    

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.text = 'Retira\n carta'
        self.bind(on_press=self.button_click)

    def button_click(self, instance):
        card = random.choice(self.cards_desafios)
        self.text = card

class DrawButtonAcao(Button):
    cards = ['Carta 1', 'Carta 2', 'Carta 3', 'Carta 4', 'Carta 5']
    cards_acoes = [
        'COMPARTILHAR',
        'ELOGIAR',
        'VOTAR',
        'NEGOCIAR',
        'CURAR',
        'COOPERAR',
        'CANTAR',
        'SUBVERTER',
        'ALIMENTAR',
        'CRIAR',
    ]    

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.text = 'Retira\n carta'
        self.bind(on_press=self.button_click)

    def button_click(self, instance):
        card = random.choice(self.cards_acoes)
        self.text = card

kv = Builder.load_file('new_window.kv')

class CardGameApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    CardGameApp().run()