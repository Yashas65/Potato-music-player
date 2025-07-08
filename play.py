from kivy.uix.screenmanager import Screen
import pygame

class Play(Screen):


    def load(self, song_path):
        self.current_song = song_path
        pygame.mixer.music.load(song_path)

    def play(self):
        if self.current_song:
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
