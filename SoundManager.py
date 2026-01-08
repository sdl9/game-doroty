## Toca efeitos sonosors (mastigação, vitória, ronco, etc)

import pygame
import os

class SoundManager:
    def __init__(self):
        dir_principal = os.path.dirname(__file__)
        dir_sons = os.path.join(dir_principal, 'assets', 'sounds')

        # Carregando sons de efeitos
        self.som_comer = pygame.mixer.Sound(os.path.join(dir_sons, 'eat.wav'))
        self.som_pum1 = pygame.mixer.Sound(os.path.join(dir_sons, 'fart-2.wav'))
        self.som_pum2 = pygame.mixer.Sound(os.path.join(dir_sons, 'fart-eco.wav'))
        self.som_derrota = pygame.mixer.Sound(os.path.join(dir_sons, 'fart-meme.wav'))
        self.som_vitoria = pygame.mixer.Sound(os.path.join(dir_sons, 'yay.wav'))
        self.som_menu = pygame.mixer.Sound(os.path.join(dir_sons, 'button-sound.wav'))

        # Músicas de fundo
        self.musica_menu = os.path.join(dir_sons, 'first-screen.mp3')
        self.musica_city = os.path.join(dir_sons, 'street.mp3')
        self.musica_derrota = os.path.join(dir_sons, 'sad-violin.mp3')
        self.musica_vitoria = os.path.join(dir_sons, 'victory.mp3')

    # Efeitos
    def play_eat_sound(self):
        self.som_comer.play()

    def play_pum1_sound(self):
        self.som_pum1.play()

    def play_pum2_sound(self):
        self.som_pum2.play()

    def play_derrota_sound(self):
        self.som_derrota.play()

    def play_vitoria_sound(self):
        self.som_vitoria.play()

    def play_menu_sound(self):
        self.som_menu.play()

    # Músicas de fundo
    def play_menu_music(self):
        pygame.mixer.music.load(self.musica_menu)
        pygame.mixer.music.play(-1) # -1 pra tocar infinitamente

    def play_city_music(self):
        pygame.mixer.music.load(self.musica_city)
        pygame.mixer.music.play(-1)

    def play_derrota_music(self):
        pygame.mixer.music.load(self.musica_derrota)
        pygame.mixer.music.play(-1)

    def play_vitoria_music(self):
        pygame.mixer.music.load(self.musica_vitoria)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()