
from kivy.uix.screenmanager import Screen
import time
#from kivy.core.audio import SoundLoader
from threading import Thread    
from kivy.clock import Clock   
from ffpyplayer.player import MediaPlayer

class Play(Screen):
    player = None
    playing = False

    def play (self,source):
        def in_thread():
            self.player = MediaPlayer(source)
            self.playing = True
            while self.playing:
                frame, val = self.player.get_frame()
                if val == 'eof':
                    break

                #Clock.schedule_once(lambda dt: self.update_ui(), 0)
            
        Thread(target=in_thread , daemon=True).start()

    def pause(self):
        if self.player:
            self.player.set_pause(True)
            self.playing = False

    def resume(self):
        if self.player:
            self.player.set_pause(False)
            self.playing = True
            def in_thread():
                while self.playing:
                    frame, val = self.player.get_frame()
                    if val == 'eof':
                        break

                    #Clock.schedule_once(lambda dt: self.update_ui(), 0)
                
            Thread(target=in_thread , daemon=True).start()

