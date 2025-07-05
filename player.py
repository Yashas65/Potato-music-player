from pathlib import Path



from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import pygame

class Play(Screen):
    def startup(self):                 
        pygame.mixer.init()
        self.current_song = None

    def load(self, song_path):
        self.current_song = song_path
        pygame.mixer.music.load(song_path)

    def play(self):
        if self.current_song:
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()



class Player(Screen):
    def on_enter(self):
        self.choose_music()
    def choose_music(self):
        c = self.ids.choose_songs
        c.clear_widgets()
        folder = Path("songs/")
        for song in folder.iterdir():
            if song.is_file():
                song_path = str(song)
                btn = Button(
                    text=song.name,
                    size_hint_y=None,
                    height=20,
                    on_press=lambda instance, path=song_path: self.play_song(path)
                )
                c.add_widget(btn)

    def play_song(self, song_path):
        play_screen = self.manager.get_screen('controls')
        play_screen.load(song_path)
        play_screen.play()
