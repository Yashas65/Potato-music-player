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
            Thread(target=self.downloading , args=(url,) , daemon=True).start()
            
        
        
    def downloading(self , url):
        path=os.path.join(os.getcwd(), 'songs')
   
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'outmpl': os.path.join(path , '%(title)s.%(ext)s'),
            'quiet': True
            
        }
        #status updation is not working for now
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            Clock.schedule_once(lambda dt: self.ids.status.text = "Download complete")

        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_status(f" error {str(e)}"))


    