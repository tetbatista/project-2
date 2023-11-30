# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.config import Config

Config.set('graphics', 'background_color', '0, 0, 0, 0')

class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)

        # Adiciona uma imagem à tela


class TelaApp(App):
    def build(self):
        return Tela()


if __name__ == '__main__':
    TelaApp().run()
