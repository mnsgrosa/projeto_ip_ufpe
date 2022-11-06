import pygame, sys
import math
from pygame import Vector2
from pygame.transform import scale
from random import randint


class Inimigo():
    def __init__(self, jogador):
        self.w, self.h = pygame.display.get_surface().get_size()
        x, y = randint(0, w - 40), randint(0, h - 60)

        while x != jogador.rect.x and y != jogador.rect.y:
            x, y = randint(0, w - 40), randint(0, h - 60)

        self.morto = False
        self.angle = math.atan2(self.pos.y - jogador.rect.y, self.pos.x - jogador.rect.x)
        self.dx = math.cos(angle) * self.w // 40
        self.dy = math.sin(angle) * self.w // 40
        self.spritesheet = scale(pygame.image.load('sprites/sprite_inimigo.png'), (240, 240))
        self.contador = -0.5
        self.sprites_esquerda = [self.spritesheet.subsurface((0, 0), (40, 60)),
                                 self.spritesheet.subsurface((40, 0), (40, 60)),
                                 self.spritesheet.subsurface((80, 0), (40, 60)),
                                 self.spritesheet.subsurface((120, 0), (40, 60)),
                                 self.spritesheet.subsurface((160, 0), (40, 60)),
                                 self.spritesheet.subsurface((200, 0), (40, 60))]
        self.sprites_direita = [self.spritesheet.subsurface((0, 60), (40, 60)),
                                self.spritesheet.subsurface((40, 60), (40, 60)),
                                self.spritesheet.subsurface((80, 60), (40, 60)),
                                self.spritesheet.subsurface((120, 60), (40, 60)),
                                self.spritesheet.subsurface((160, 60), (40, 60)),
                                self.spritesheet.subsurface((200, 60), (40, 60)),]
        self.sprites_baixo = [self.spritesheet.subsurface((0, 120), (40, 60)),
                              self.spritesheet.subsurface((40, 120), (40, 60)),
                              self.spritesheet.subsurface((80, 120), (40, 60)),
                              self.spritesheet.subsurface((120, 120), (40, 60)),
                              self.spritesheet.subsurface((160, 120), (40, 60)),
                              self.spritesheet.subsurface((200, 120), (40, 60))]
        self.sprites_cima = [self.spritesheet.subsurface((0, 180), (40, 60)),
                             self.spritesheet.subsurface((40, 180), (40, 60)),
                             self.spritesheet.subsurface((80, 180), (40, 60)),
                             self.spritesheet.subsurface((120, 180), (40, 60)),
                             self.spritesheet.subsurface((160, 180), (40, 60)),
                             self.spritesheet.subsurface((200, 180), (40, 60))]
        self.image = self.sprites_baixo[0]
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_inimigo(self, jogador, bala):
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

        if ((self.cos > 0 and self.cos < 1) and (self.sin < 1 and self.sin > 0)) or (
                (self.cos > 0 and self.cos < 1) and (self.sin > -1 and self.sin < 0)):
            return 'direita'

        if self.cos == 0 and self.sin == 1:
            return 'cima'

        if ((self.cos < 0 and self.cos > -1) and (self.sin < 1 and self.sin > 0)) or (
                (self.cos > -1 and self.cos < 0) and (self.sin > -1 and self.sin < 0)):
            return 'esquerda'

        if self.cos == 0 and self.sin == -1:
            return 'baixo'

    def draw(self, jogador, bala):
        self.contador += 0.5
        if self.contador == 6:
            self.contador = 0
        direcao = self.update_inimigo(jogador, bala)
        if direcao == 'direita':
            self.image = self.sprites_direita[int(self.contador)]
        elif direcao == 'cima':
            self.image = self.sprites_cima[int(self.contador)]
        elif direcao == 'esquerda':
            self.image = self.sprites_esquerda[int(self.contador)]
        elif direcao == 'baixo':
            self.image = self.sprites_baixo[int(self.contador)]
