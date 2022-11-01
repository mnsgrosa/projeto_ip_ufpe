import pygame
from pygame.math import Vector2
from pygame.transform import scale
from random import randint


class Pontos(pygame.sprite.Sprite):
    def __init__(self):
        # Para teste até que se tenha a classe inimigo
        pygame.sprite.Sprite.__init__(self)
        self.item_droppado = False
        self.tempo_spawn = 0
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.contador = 0
        self.indice = -1
        self.coin_0, self.coin_1 = pygame.image.load('sprites/coin_0.png'), pygame.image.load('sprites/coin_1.png')
        self.coin_2, self.coin_3 = pygame.image.load('sprites/coin_2.png'), pygame.image.load('sprites/coin_3.png')
        self.coin_4, self.coin_5 = pygame.image.load('sprites/coin_4.png'), pygame.image.load('sprites/coin_5.png')
        self.coin_0, self.coin_1 = scale(self.coin_0, (35, 35)), scale(self.coin_1, (35, 35))
        self.coin_2, self.coin_3 = scale(self.coin_2, (35, 35)), scale(self.coin_3, (35, 35))
        self.coin_4, self.coin_5 = scale(self.coin_4, (35, 35)), scale(self.coin_5, (35, 35))
        self.sprites = (self.coin_0, self.coin_1, self.coin_2, self.coin_3, self.coin_4, self.coin_5)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(topleft=(2000, 0))
        self.pos = Vector2(randint(0, self.largura_tela - 35), randint(0, self.altura_tela - 35))

    def spawn_ponto(self, coleta_ponto):
        if coleta_ponto:
            self.item_droppado = False
            self.rect.x, self.rect.y = 2000, 0
        if self.item_droppado:
            self.tempo_spawn = 0
        elif not self.item_droppado and self.tempo_spawn < 30:
            self.tempo_spawn += 1
        elif not self.item_droppado and self.tempo_spawn >= 30:
            self.pos = Vector2(randint(0, self.largura_tela - 35), randint(0, self.altura_tela - 35))
            self.rect.x, self.rect.y = self.pos.x, self.pos.y
            self.item_droppado = True

    def animacao(self):
        if self.item_droppado:
            self.contador += 1
            if self.contador >= 3:
                self.contador = 0
                self.indice += 1
                if self.indice > 5:
                    self.indice = 0
                self.image = self.sprites[self.indice]
                self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

    def update_ponto(self, coleta_ponto):
        self.spawn_ponto(coleta_ponto)
        self.animacao()

