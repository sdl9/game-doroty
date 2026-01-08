## Representa as comidas que vêm do lado direito
import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela):
        super().__init__()
        # Escolhe uma imagem aleatória de comida
        import random
        img_id = random.randint(1, 6)
        dir_principal = os.path.dirname(__file__)
        img_path = os.path.join(dir_principal, 'assets', 'food', f'{img_id}.png')
        self.image = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        # Spawna no lado direito, em uma altura aleatória
        self.rect.x = largura_tela
        spawn_top = 208  # mesmo valor do Player
        spawn_bot = altura_tela - self.rect.height
        self.rect.y = random.randint(spawn_top, spawn_bot)
        self.velocidade = 8  # Velocidade que a comida anda para a esquerda

    def update(self):
        # Move a comida para a esquerda
        self.rect.x -= self.velocidade
    
    def draw(self, tela):
        tela.blit(self.image, self.rect)