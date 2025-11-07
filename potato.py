from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from a_musc import Add_Music
from player import Player
from play import Play


Builder.load_file('a_musc.kv')
Builder.load_file('player.kv')
Builder.load_file('play.kv')

class Home(Screen):
    pass


class Potato(App):
    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        sm.add_widget(Add_Music(name='add_music'))
        sm.add_widget(Player(name='player'))
        sm.add_widget(Play(name='play'))
        return sm
Potato().run()