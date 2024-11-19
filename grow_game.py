from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
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

class CartaValor2Cartas(Screen):
    pass

class CartaDesafio2Cartas(Screen):
    pass

class CartaValor3Cartas(Screen):
    pass

class CartaDesafio3Cartas(Screen):
    pass

class CartaAcao3Cartas(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class DrawButton(Button):
    cards = ['Carta 1', 'Carta 2', 'Carta 3', 'Carta 4', 'Carta 5']

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.text = 'Retira\n carta'
        self.bind(on_press=self.button_click)

    def button_click(self, instance):
        card = random.choice(self.cards)
        self.text = card

class GamePage(BoxLayout):

    def __init__(self, **kwargs):
        super(GamePage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Carta de Valor', font_size=25)
        self.add_widget(self.label)
        btn = DrawButton()
        self.add_widget(btn)

kv = Builder.load_file('new_window.kv')

class MainPage(BoxLayout):

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Grow-a-Game Brasil', font_size=40)
        self.add_widget(self.label)

        btn = Button(text='Pressione aqui para iniciar o jogo')
        btn.bind(on_press=self.card_clicked)
        self.add_widget(btn)

    def card_clicked(self, instance):
        self.label.text = 'Você clicou na carta!'
        

class CardGameApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    CardGameApp().run()