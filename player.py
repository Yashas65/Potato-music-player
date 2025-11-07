
from pathlib import Path
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen , ScreenManager
from threading import Thread
from kivy.clock import Clock
import play
from kivy.app import App


class Player(Screen):
    def on_enter(self):
        self.choose_music()
    def choose_music(self):
        scrollable_frame = self.ids.choose_songs
        scrollable_frame.clear_widgets()
        folder = Path("songs/")
        if not folder.exists():
            folder.mkdir()
        for song in folder.iterdir():
            if song.is_file():
                
                sang = str(song)#sang basically means song , i was not able to think of anyother name for variable
                controls = play.Play()
                btn = Button(
                    text=song.name,
                    size_hint_y=None,
                    height=20,
                    on_press=lambda x,y=sang : controls.play(y) 
                    #on_press=lambda instance, path=sang: App.get_running_app().root.get_screen('play').load(path)
                          
                )
                scrollable_frame.add_widget(btn)

