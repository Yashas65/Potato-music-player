from pathlib import Path



from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen , ScreenManager
import pygame
from play import Play


class Player(Screen):
    def on_enter(self):
        self.choose_music()
    def choose_music(self):
        scrollable_frame = self.ids.choose_songs
        scrollable_frame.clear_widgets()
        folder = Path("songs/")
        
        for song in folder.iterdir():
            if song.is_file():
                
                sang = str(song)#sang basically means song , i was not able to think of anyother name for variable
                btn = Button(
                    text=song.name,
                    size_hint_y=None,
                    height=20,
                    on_press=lambda x , y=sang: Play.load(y)
                )
                scrollable_frame.add_widget(btn)

