from kivy.uix.screenmanager import Screen
import time
from threading import Thread    
from kivy.clock import Clock   
from ffpyplayer.player import MediaPlayer

class Play(Screen):
    
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

    def pause(self):
        try:
            print('pause working')
            player.set_pause(True)
            self.playing = False
        except Exception as e:
            print('Error pausing:', e)
    def resume(self):
        try:
            player.set_pause(False)
            self.playing = True
        except Exception as e:
            print('Error resuming:', e)