## Controla loop principal, eventos, pontuação e troca de telas

import pygame
from pygame.locals import * # * == dentro do submodel locals eu vou estar importando todas as funções e todas as constantes de locals;
from sys import exit # quando clicar pra fechar janela, a função é chamada e fecha a janela;
from random import randint #importando funcao que sorteia valores
import os
from SoundManager import SoundManager
from ScreenManager import ScreenManager
from Player import Player
from Obstacle import Obstacle

#TODO: Versionar software no github

class Game:
    def __init__(self):
        pygame.init()
        self.largura = 640
        self.altura = 480
        self.tela = pygame.display.set_mode((self.largura,self.altura))
        self.menu_img = pygame.image.load('assets/telas/tela-inicio.gif').convert_alpha()
        self.menu_img = pygame.transform.scale(self.menu_img, (int(self.largura * 1.5), int(self.altura * 1.5)))
        self.background = pygame.image.load('assets/telas/background-1.jpg').convert()
        self.vitoria = pygame.image.load('assets/telas/tela-vitoria.jpg').convert()
        self.derrota = pygame.image.load('assets/telas/tela-derrota.jpg').convert()
        pygame.display.set_caption('Passeio com a Doroty')
        self.fps = pygame.time.Clock()
        self.vidas = 3
        self.estado = "menu"
        self.sound_manager = SoundManager()
        self.screen_manager = ScreenManager(self.largura, self.altura)
        self.player = Player()
        self.obstacles = []
        self.spawn_timer = 0
        self.ultimo_estado = None
        self.menu_selecionado = 0  # 0 = Jogar, 1 = Sair
        
    def run(self):    
        print("Rodando o jogo...")
        while True:
            if self.estado != self.ultimo_estado:
                # Toca a música do estado atual
                # Para música anterior antes de tocar a nova
                pygame.mixer.music.stop()
                if self.estado == "menu":
                    self.sound_manager.play_menu_music()
                elif self.estado == "jogando":
                    self.sound_manager.play_city_music()
                elif self.estado == "derrota":
                    self.sound_manager.play_derrota_music()
                elif self.estado == "vitoria":
                    self.sound_manager.play_vitoria_music()
                self.ultimo_estado = self.estado

            # --- MENU ---
            if self.estado == "menu":
                self.tela.fill((255,255,255))
                fonte_titulo = pygame.font.Font('assets/game-font.otf', 40)
                fonte_sub = pygame.font.Font('assets/game-font.otf', 25)
                self.screen_manager.draw_menu(self.tela, self.menu_img, fonte_titulo, fonte_sub, self.menu_selecionado)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key in [pygame.K_UP, pygame.K_w]:
                            self.menu_selecionado = (self.menu_selecionado - 1) % 2
                        if event.key in [pygame.K_DOWN, pygame.K_s]:
                            self.menu_selecionado = (self.menu_selecionado + 1) % 2
                        if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                            if self.menu_selecionado == 0:
                                self.estado = "como-jogar"
                            elif self.menu_selecionado == 1:
                                pygame.quit()
                                exit()
                continue

            # --- COMO JOGAR ---
            if self.estado == "como-jogar":
                fonte_titulo = pygame.font.Font('assets/game-font.otf', 40)
                fonte_sub = pygame.font.Font('assets/game-font.otf', 25)
                self.screen_manager.draw_como_jogar(self.tela, self.background, fonte_titulo, fonte_sub)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        self.estado = "jogando"
                continue

            # --- VITÓRIA ---
            if self.estado == "vitoria":
                if self.ultimo_estado != "vitoria":
                    self.sound_manager.play_vitoria_sound()
                fonte_titulo = pygame.font.Font('assets/game-font.otf', 40)
                fonte_sub = pygame.font.Font('assets/game-font.otf', 25)
                self.screen_manager.draw_vitoria(self.tela, self.vitoria, fonte_titulo, fonte_sub)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        self.estado = "menu"
                        self.vidas = 3
                        self.obstacles = []
                        self.tempo_restante = 60  # reseta timer
                continue

            # --- DERROTA ---
            if self.estado == "derrota":
                if self.ultimo_estado != "derrota":
                    self.sound_manager.play_derrota_sound()
                fonte_titulo = pygame.font.Font('assets/game-font.otf', 40)
                fonte_sub = pygame.font.Font('assets/game-font.otf', 25)
                self.screen_manager.draw_derrota(self.tela, self.derrota, fonte_titulo, fonte_sub)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        pygame.mixer.music.stop()  # Para a música ao sair da derrota
                        self.estado = "menu"
                        self.vidas = 3
                        self.obstacles = []
                        self.tempo_restante = 60  # reseta timer
                        self.sound_manager.play_menu_music()  # Toca música do menu
                self.ultimo_estado = self.estado
                continue

            # --- JOGANDO ---
            self.fps.tick(30)
            self.tela.fill((255,255,255))
            self.tela.blit(self.background, (0,0))

            # Atualiza timer
            if not hasattr(self, 'tempo_restante'):
                self.tempo_restante = 60
            if not hasattr(self, 'ultimo_tick'):
                self.ultimo_tick = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            if now - self.ultimo_tick >= 1000:
                self.tempo_restante -= 1
                self.ultimo_tick = now
            if self.tempo_restante <= 0:
                self.estado = "vitoria"

            # Mostra timer na tela (fonte padrão do sistema)
            fonte_timer = pygame.font.SysFont(None, 36)
            texto_timer = fonte_timer.render(f"Tempo: {self.tempo_restante}s", True, (255, 0, 0))
            self.tela.blit(texto_timer, (self.largura-180, 10))

            # Mostra vidas como X X X
            fonte_vidas = pygame.font.Font('assets/game-font.otf', 30)
            vidas_str = ' '.join(['X'] * self.vidas)
            texto_vidas = fonte_vidas.render(vidas_str, True, (255, 0, 0))
            self.tela.blit(texto_vidas, (10, 40))

            # Spawn de comidas
            if self.spawn_timer == 0:
                self.spawn_timer = 25
                obstacle = Obstacle(self.largura, self.altura)
                self.obstacles.append(obstacle)
            else:
                self.spawn_timer -= 1

            # Atualiza e desenha as comidas
            for obstacle in self.obstacles[:]:
                obstacle.update()
                obstacle.draw(self.tela)
                if self.player.rect.colliderect(obstacle.rect):
                    #self.sound_manager.play_eat_sound()
                    import random
                    if random.choice([True, False]):
                        self.sound_manager.play_pum1_sound()
                    else:
                        self.sound_manager.play_pum2_sound()
                    self.obstacles.remove(obstacle)
                    self.vidas -= 1
                    
                    # Verifica se perdeu
                    if self.vidas <= 0:
                        self.estado = "derrota"

            # Remove comidas que saíram da tela
            self.obstacles = [obs for obs in self.obstacles if obs.rect.x > -obs.rect.width]

            # Player
            keys = pygame.key.get_pressed()
            self.player.update(keys, self.altura, self.largura)
            self.player.draw(self.tela)

            # Mostra vidas restantes
            fonte_vidas = pygame.font.Font('assets/game-font.otf', 30)
            texto_vidas = fonte_vidas.render(f"Vidas: {self.vidas}", True, (255, 0, 0))
            self.tela.blit(texto_vidas, (10, 10))

            # Eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()

if __name__ == "__main__":
    jogo = Game()
    jogo.run()          