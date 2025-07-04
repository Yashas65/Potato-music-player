from kivy.uix.screenmanager import Screen
import yt_dlp 
import os
from pathlib import Path
from kivy.clock import Clock
from threading import Thread

"""
                ERRORS
            STATUS UPDATION AFTER DOWNLOAD
                AND PROBABLY THAT IS NOT DOWNLOADING THE FILE
                
"""




class Add_Music(Screen):
    def download(self):
        url = self.ids.url.text

        if not url:
            self.ids.status.text = "please enter a url"
            return
        else:
            self.ids.status.text = "Downloading"
            Thread(target=self.download , args=(url,) , daemon=True).start()
            
        
        
        path = os.path.join(os.getcwd(), 'songs')
        os.makedirs(path, exist_ok=True)  # Ensure the directory exists
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'outtmpl': os.path.join(path , '%(title)s.%(ext)s'),
            'quiet': True
            
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)
            def set_status_complete(dt):
                self.ids.status.text = "Download complete"
            Clock.schedule_once(set_status_complete)
        except Exception as e:
            def set_status_error(dt):
                self.ids.status.text = "error"
            Clock.schedule_once(set_status_error)
            print(e)

    