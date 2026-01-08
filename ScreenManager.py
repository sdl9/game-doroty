# Gera as imagens de início, vitória e derrota

import pygame
import os

class ScreenManager:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        # Carrega as imagens do menu
        self.menu_faces = []
        for i in range(1, 7):
            img = pygame.image.load(f'assets/capa/{i}.png').convert_alpha()
            w, h = img.get_width(), img.get_height()
            self.menu_faces.append(img)

    def draw_menu(self, tela, menu_img, fonte_titulo, fonte_sub, selecionado):
        tela.fill((255,255,255))
        #tela.blit(background, (0,0))
        img_rect = menu_img.get_rect(center=(self.largura//2, self.altura//2 - 60))
        tela.blit(menu_img, img_rect)
        # Canto superior esquerdo
        tela.blit(self.menu_faces[2], (10, 10))
        # Canto superior direito
        tela.blit(self.menu_faces[5], (self.largura-150, 10))
        # Canto inferior esquerdo
        tela.blit(self.menu_faces[1], (10, self.altura-150))
        # Canto inferior direito
        tela.blit(self.menu_faces[0], (self.largura-130, self.altura-150))
        cor_jogar = (0, 100, 0) if selecionado == 0 else (0, 0, 0)
        cor_sair = (100, 0, 0) if selecionado == 1 else (0, 0, 0)
        jogar_txt = fonte_sub.render("JOGAR", True, cor_jogar)
        sair_txt = fonte_sub.render("SAIR", True, cor_sair)
        tela.blit(jogar_txt, (self.largura//2 - 50, self.altura//2 + 120))
        tela.blit(sair_txt, (self.largura//2 - 50, self.altura//2 + 160))

        # Título
        texto = fonte_titulo.render("Passeio com a Doroty", True, (0, 0, 0))
        texto_rect = texto.get_rect(center=(self.largura // 2, self.altura // 2 + 40))
        tela.blit(texto, texto_rect)
        texto2 = fonte_sub.render("Pressione qualquer tecla para comecar", True, (0, 0, 0))
        texto2_rect = texto2.get_rect(center=(self.largura // 2, self.altura // 2 + 90))
        tela.blit(texto2, texto2_rect)
        
    def draw_como_jogar(self, tela, background, fonte_titulo, fonte_sub):
        tela.fill((255,255,255))
        tela.blit(background, (0,0))
        texto = fonte_titulo.render("Como Jogar", True, (0, 128, 0))
        tela.blit(texto, (self.largura//2 - texto.get_width()//2, 70))
        instrucoes = [
            "Voce recebeu a missao de passear com a Doroty!",
            "Nao deixe que ela coma comida da rua, ou tera que arcar",
            "com as custas do veterinario!",
            "",
            "Mova ela com WASD.",
            "Fuja das comidas que irao surgir na tela por um minuto!",
            "Se encostar em tres comidas perde.",
            "",
            "Pressione qualquer tecla para comecar"
        ]
        y = 130
        for linha in instrucoes:
            txt = fonte_sub.render(linha, True, (255,255,255))
            tela.blit(txt, (self.largura//2 - txt.get_width()//2, y))
            y += 35

    def draw_derrota(self, tela, derrota, fonte_titulo, fonte_sub):
        tela.fill((255,255,255))
        tela.blit(derrota, (0,0))
        texto = fonte_titulo.render("GAME OVER", True, (255, 0, 0))
        tela.blit(texto, (self.largura//2 - texto.get_width()//2, self.altura//2 - 40))
        texto2 = fonte_sub.render("Doroty comeu demais e passou mal)", True, (255, 255, 255))
        tela.blit(texto2, (self.largura//2 - texto2.get_width()//2, self.altura//2 + 10))
        texto3 = fonte_sub.render("Pressione qualquer tecla para voltar ao menu", True, (255, 255, 255))
        tela.blit(texto3, (self.largura//2 - texto3.get_width()//2, self.altura//2 + 60))

    def draw_vitoria(self, tela, vitoria, fonte_titulo, fonte_sub):
        tela.fill((255,255,255))
        tela.blit(vitoria, (0,0))
        texto = fonte_titulo.render("VITORIA!", True, (0, 255, 0))
        tela.blit(texto, (self.largura//2 - texto.get_width()//2, self.altura//2 - 40))
        texto2 = fonte_sub.render("Passeio concluido com sucesso! Agora e so relaxar", True, (0, 0, 0))
        tela.blit(texto2, (self.largura//2 - texto2.get_width()//2, self.altura//2 + 10))
        texto3 = fonte_sub.render("Pressione qualquer tecla para voltar ao menu", True, (0, 0, 0))
        tela.blit(texto3, (self.largura//2 - texto3.get_width()//2, self.altura//2 + 60))