from pathlib import Path



from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
class Player(Screen):
    def on_enter(self):
        self.choose_music()
    def choose_music(self):
        c = self.ids.choose_songs
        folder = Path("songs/")

        for song in folder.iterdir():
            if song.is_file():
                name = str(song)
                name.split()
                print(name)
                c.add_widget(Button(text=f"{song}" , size_hint_y=None))
    

