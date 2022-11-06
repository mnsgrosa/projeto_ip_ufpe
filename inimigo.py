from pygame import Vector2
from random import randint
import pygame, sys
import math


# INIMIGO

class Inimigo:
    def __init__(self, jogador):
        self.w, self.h = pygame.display.get_surface().get_size()
        
        x = randint(0, w)
        y = randint(0, h)

        while x != jogador.rect.x and y != jogador.rect.y:
            x = randint(0, w)
            y = randint(0, h)

        self.pos = Vector2(x, y)
        self.morto = False
        self.angle = math.atan2(self.pos.y - jogador.rect.y, self.pos.x - jogador.rect.x)
        self.dx = math.cos(angle) * self.w // 40
        self.dy = math.sin(angle) * self.w // 40
        self.image = pygame.Surface((45, 75))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def update(self, jogador, bala):
        self.angle = math.atan2(self.rect.y - jogador.rect.y, self.rect.x - jogador.rect.x)
        self.cos = math.cos(self.angle)
        self.sin = math.sin(self.angle)
        self.dx = self.cos * self.w // 40
        self.dy = self.sin * self.w // 40
        self.rect.x += self.dx
        self.rect.y += self.dy

        if bala.rect.colliderect(self.rect):
            self.morto = True
            self.posicao_morto = (self.rect.x, self.rect.y)
        else:
            self.morto = False

        if ((self.cos > 0 and self.cos < 1) and (self.sin < 1 and self.sin > 0)) or ((self.cos > 0 and self.cos < 1) and (self.sin > -1 and self.sin < 0)):
            return 'direita', self.morto, self.posicao_morto
        
        if self.cos == 0 and self.sin == 1:
            return 'cima', self.morto, self.posicao_morto
        
        if ((self.cos < 0 and self.cos > -1) and (self.sin < 1 and self.sin > 0)) or ((self.cos > -1 and self.cos < 0) and (self.sin > -1 and self.sin < 0)):
            return 'esquerda', self.morto, self.posicao_morto

        if self.cos == 0 and self.sin == -1:
            return 'baixo', self.morto, self.posicao_morto

    def draw(self, jogador, bala):
        direcao = self.update(jogador, bala)
        if direcao == 'direita':
            pass
        elif direcao == 'cima':
            pass
        elif direcao == 'esquerda':
            pass
        elif direcao == 'baixo':
            pass