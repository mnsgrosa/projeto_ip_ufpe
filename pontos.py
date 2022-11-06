import pygame
from pygame.math import Vector2
from pygame.transform import scale
from random import randint


class Pontos():
    def __init__(self):
        pygame.mixer.init()
        self.tempo_spawn = 0
        self.tela = pygame.display.get_surface()
        self.largura_tela, self.altura_tela = pygame.display.get_surface().get_size()
        self.contador = 1 / 4
        self.som = pygame.mixer.Sound('sons/som_moeda.wav')
        self.coin_0, self.coin_1 = pygame.image.load('sprites/coin_0.png'), pygame.image.load('sprites/coin_1.png')
        self.coin_2, self.coin_3 = pygame.image.load('sprites/coin_2.png'), pygame.image.load('sprites/coin_3.png')
        self.coin_4, self.coin_5 = pygame.image.load('sprites/coin_4.png'), pygame.image.load('sprites/coin_5.png')
        self.coin_0, self.coin_1 = scale(self.coin_0, (35, 35)), scale(self.coin_1, (35, 35))
        self.coin_2, self.coin_3 = scale(self.coin_2, (35, 35)), scale(self.coin_3, (35, 35))
        self.coin_4, self.coin_5 = scale(self.coin_4, (35, 35)), scale(self.coin_5, (35, 35))
        self.lista_ponto = []
        self.sprites = [self.coin_0, self.coin_1, self.coin_2, self.coin_3, self.coin_4, self.coin_5]
        self.image = self.sprites[0]

    #morte_inimigo é uma variável booleana
    def spawn_ponto(self, morte_inimigo, pos_inimigo_morto):
        if morte_inimigo:
            self.lista_ponto.append(pos_inimigo_morto)
        for ponto in self.lista_ponto:
            self.tela.blit(self.image, ponto)

    #idx_ponto_coletado é o índice do sprite q sofreu a colisão
    def coleta_ponto(self, ponto_coletado):
        contador = -1
        for ponto in self.lista_ponto:
            contador += 1
            if ponto == ponto_coletado:
                self.som.play()
                del self.lista_ponto[contador]

    def animacao(self):
        if self.contador == 6:
            self.contador = 0
        self.image = self.sprites[int(self.contador)]
        self.contador += 1 / 4

    def update_ponto(self, morte_inimigo, pos_inimigo_morto, ponto_coletado):
        self.animacao()
        self.spawn_ponto(morte_inimigo, pos_inimigo_morto)
        self.coleta_ponto(ponto_coletado)
