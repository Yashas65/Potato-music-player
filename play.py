from kivy.uix.screenmanager import Screen
import pygame

class Play(Screen):



    def load(self):#load and play
        pygame.mixer.music.load(self)
        pygame.mixer.music.play()

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
