## Representa a Doroty -- posição, movimento, imagem, colisões
import pygame
from pygame.locals import *
from sys import exit
import os
from Obstacle import Obstacle
from SoundManager import SoundManager

pygame.display.set_caption('Sprites')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites_doty = []
        dir_principal = os.path.dirname(__file__)
        dir_sprites = os.path.join(dir_principal, 'assets', 'sprites')  # Caminho para as imagens da Doroty

        # Carrega as imagens do rosto da Doroty na lista
        for i in range(1, 5):
            img = pygame.image.load(os.path.join(dir_sprites, f'{i}.png')).convert_alpha()
            img = pygame.transform.scale(img, (64, 64))
            self.sprites_doty.append(img)

        self.current_sprite = 0  # Índice do sprite atual (para animação)
        self.image = self.sprites_doty[self.current_sprite]  # Imagem a ser desenhada
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 208)  # Posição inicial
        self.velocidade = 8

    def draw(self, tela):
        # Desenha a imagem atual na posição atual
        tela.blit(self.image, self.rect)

    def update(self, keys, altura_tela, largura_tela):
        # Limite superior: onde ela spawna (não deixa subir mais que isso)
        spawn_top = 208  # mesmo valor do self.rect.topleft no __init__
        mudou = False  # Para saber se está andando e animar

        # Para cima
        if keys[pygame.K_w] and self.rect.top > spawn_top:
            self.rect.y -= self.velocidade
            mudou = True
        # Para baixo
        if keys[pygame.K_s] and self.rect.bottom < altura_tela:
            self.rect.y += self.velocidade
            mudou = True
        # Para esquerda
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocidade
            mudou = True
        # Para direita
        if keys[pygame.K_d] and self.rect.right < largura_tela:
            self.rect.x += self.velocidade
            mudou = True

        # Animação: troca de sprite se estiver andando
        if mudou:
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites_doty)
            self.image = self.sprites_doty[self.current_sprite]
        else:
            # Se não estiver andando, volta para o sprite parado
            self.current_sprite = 0
            self.image = self.sprites_doty[self.current_sprite]
