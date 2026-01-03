from pathlib import Path
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen , ScreenManager
from threading import Thread
from kivy.clock import Clock
import play
from kivy.app import App
from kivy.uix.screenmanager import SlideTransition , FadeTransition


class Player(Screen):
    
    #ui buttons
    def go_to_add_music(self):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = 'add_music'
    playing = False

    def play (self,source):
        def in_thread():
            global player
            player = MediaPlayer(source)
            self.playing = True
            while self.playing:
                frame, val = player.get_frame()
                if val == 'eof':
                    break

            
        Thread(target=in_thread , daemon=True).start()

    def toggle(self):
        
        button  = self.ids.toggle #id of the toggle btn

        #pauseing , means self.playing is true
        if self.playing:
            try:
                player.set_pause(True)
                self.playing = False
                button.text = '|>'
            except Exception as e:
                print('Error pausing:', e)
    
        else:
            try:
                player.set_pause(False)
                self.playing = True
                button.text = '||'

            except Exception as e:
                print('Error resuming:', e)
