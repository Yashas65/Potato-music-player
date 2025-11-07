
from kivy.uix.screenmanager import Screen
import time
#from kivy.core.audio import SoundLoader
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

                #Clock.schedule_once(lambda dt: self.update_ui(), 0)
            
        Thread(target=in_thread , daemon=True).start()

    def pause(self):
        #if self.player:
        try:
            print('pause working')
            player.set_pause(True)
            self.playing = False
        except Exception as e:
            print('Error pausing:', e)
    def resume(self):
        #if self.player:
        try:
            player.set_pause(False)
            self.playing = True
        except Exception as e:
            print('Error resuming:', e)