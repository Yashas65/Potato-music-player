from pathlib import Path



from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen , ScreenManager
import pygame
from play import Play


class Player(Screen):
    def on_enter(self):
        self.choose_music()
    def choose_music(self):
        c = self.ids.choose_songs
        c.clear_widgets()
        folder = Path("songs/")
        
        def play(name):
            path = folder
            play.load(path)
            ScreenManager.current_screen = 'play'
            Play.play(path)
        
        for song in folder.iterdir():
            if song.is_file():
                song_path = str(song)
                btn = Button(
                    text=song.name,
                    size_hint_y=None,
                    height=20,
                    on_press=lambda x : play(song.name)
                )
                c.add_widget(btn)

