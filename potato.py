from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from a_musc import Add_Music
from player import Player

Builder.load_file('a_musc.kv')
Builder.load_file('player.kv')
    
class Home(Screen):
    pass


class Potato(App):
    def build(self):
        s = ScreenManager()
        s.add_widget(Player(name='player'))
        s.add_widget(Add_Music(name='add_music'))
        pass

Potato().run()