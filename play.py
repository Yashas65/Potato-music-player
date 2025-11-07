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