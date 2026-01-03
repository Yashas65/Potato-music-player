from kivy.uix.screenmanager import Screen
import yt_dlp 
import os
from pathlib import Path
from kivy.clock import Clock
from threading import Thread
from kivy.uix.screenmanager import SlideTransition



class Add_Music(Screen):

    def go_to_player(self):
        self.manager.transition = SlideTransition(direction = 'left')
        self.manager.current = 'player'
    def download(self):

        url = self.ids.url.text

        if not url:
            self.ids.status.text = "please enter a url"
            return
        else:
            self.ids.status.text = "Downloading"
            Thread(target=self.downloading , args=(url,) , daemon=True).start()
            
        
        
    def downloading(self , url):
        
        try:    
           

            path = os.path.join(os.getcwd(), 'songs')
            os.makedirs(path, exist_ok=True)
            f_path = os.path.join(path, '%(title)s.mp3')

            
            class MyLogger:
               def debug(self, msg): 
                   print("[DEBUG]", msg)
               
               def warning(self, msg): 
                   print("[WARNING]", msg)
               
               def error(self, msg): 
                   print("[ERROR]", msg)

            ydl_opts = {
                'format': 'bestaudio[ext=mp3]/bestaudio', #fake mp3 just the extension
                'outtmpl': f_path,
                'quiet': True,
                'logger': MyLogger()
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            def set_status_complete(dt):
                self.ids.status.text = "Download complete"
            Clock.schedule_once(set_status_complete)
        
        except Exception as e:
            def set_status_error(dt):
                self.ids.status.text = "error"
            Clock.schedule_once(set_status_error)
            print(e)

    