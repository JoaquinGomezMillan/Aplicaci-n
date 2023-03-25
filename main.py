from kivy.app import App
from kivy.uix.label import Label

class FirstKivy(App):
    def build(self):
        return Label(text='Hola kivy!!')
    

FirstKivy().run()

Hola