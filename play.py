from kivy.uix.screenmanager import Screen
import time
from pygame.mixer import music


def updt_status(self , dis):
    self.ids.sttus = f'{dis}'
    time.sleep(0.3)
    self.ids.sttus = ''
    print(dis)

class Play(Screen):


    def load(self):#load and play
        music.load(self)
        music.set_volume(1.0)
        music.play()

    def play(self):
        try:
            music.play()
            updt_status(self ,'|>')
        except Exception as e:
            updt_status(self , e)

    def pause(self):
        music.pause()
        updt_status(self , '||')



    def in_vol(self):
        self.volume = min(1.0, self.volume+0.1)
        music.setvolume(self.volume)
        updt_status(self , '+')

    def dec_vol(self):
        self.volume = max(0.0, self.volume-0.1)
        music.setvolume(self.volume)
        updt_status(self , '-')

     