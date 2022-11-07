import pygame
from pygame.math import Vector2
from pygame.transform import scale
from random import randint


class Pontos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mixer.init()
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.tempo_spawn = 0
        self.contador = -0.25
        self.existe_sprite = True
        self.som = pygame.mixer.Sound('sons/som_moeda.wav')
        self.coin_0, self.coin_1 = pygame.image.load('sprites/coin_0.png'), pygame.image.load('sprites/coin_1.png')
        self.coin_2, self.coin_3 = pygame.image.load('sprites/coin_2.png'), pygame.image.load('sprites/coin_3.png')
        self.coin_4, self.coin_5 = pygame.image.load('sprites/coin_4.png'), pygame.image.load('sprites/coin_5.png')
        self.coin_0, self.coin_1 = scale(self.coin_0, (35, 35)), scale(self.coin_1, (35, 35))
        self.coin_2, self.coin_3 = scale(self.coin_2, (35, 35)), scale(self.coin_3, (35, 35))
        self.coin_4, self.coin_5 = scale(self.coin_4, (35, 35)), scale(self.coin_5, (35, 35))
        self.sprites = [self.coin_0, self.coin_1, self.coin_2, self.coin_3, self.coin_4, self.coin_5]
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(topleft=(randint(0, self.largura_tela - 35), randint(0, self.altura_tela - 35)))

    def spawn_ponto(self, coleta_ponto):
        if coleta_ponto:
            self.som.play()
            self.existe_sprite = False
            self.rect.x, self.rect.y = 1000, 1000
        if self.existe_sprite:
            self.tempo_spawn = 0
        elif not self.existe_sprite and self.tempo_spawn < 10:
            self.tempo_spawn += 1
        elif not  self.existe_sprite and self.tempo_spawn == 10:
            self.existe_sprite = True
            self.rect.x, self.rect.y = randint(0, self.largura_tela - 35), randint(0, self.altura_tela - 35)

    def animacao(self):
        self.contador += 0.25
        if self.contador == 6:
            self.contador = 0
        self.image = self.sprites[int(self.contador)]

    def update_ponto(self, coleta_ponto):
        self.animacao()
        self.spawn_ponto(coleta_ponto)
