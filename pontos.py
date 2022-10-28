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
        self.posicao = Vector2(randint(0, self.largura_tela - 35), randint(0, self.altura_tela - 35))
        self.image = pygame.image.load('sprites/coin_0.png')
        self.image = scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 0


    def spawn_ponto(self, coleta_ponto):
        if coleta_ponto:
            self.item_droppado = False
            self.rect.x = 2000
            self.rect.y = 0
        if self.item_droppado:
            self.tempo_spawn = 0
        elif not self.item_droppado and self.tempo_spawn < 30:
            self.tempo_spawn += 1
        elif not self.item_droppado and self.tempo_spawn >= 30:
            self.posicao = Vector2(randint(0, self.largura_tela - 35), randint(0, self.altura_tela - 35))
            self.rect.x = self.posicao.x
            self.rect.y = self.posicao.y
            self.item_droppado = True
