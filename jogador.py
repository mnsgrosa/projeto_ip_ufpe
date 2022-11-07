import pygame
import math
from pygame.math import Vector2
from pygame.transform import scale


# Note que jogador herda da classe Sprite do pygame
class Jogador(pygame.sprite.Sprite):
    # construtor da classe do jogador
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        w, h = pygame.display.get_surface().get_size()
        self.vida = 3
        self.vel = w // 40
        self.ponto = 0
        self.morto = False
        self.dano = False
        self.coleta_vida = False
        self.coleta_vel = False
        self.coleta_ponto = False
        self.contador = -0.5
        self.parado = True
        self.direcao = 'direita'
        self.spritesheet = scale(pygame.image.load('sprites/spritesheet_cangaceiro.png'), (240, 240))
        self.sprites_esquerda = [self.spritesheet.subsurface((0, 0), (40, 60)),
                                 self.spritesheet.subsurface((40, 0), (40, 60)),
                                 self.spritesheet.subsurface((80, 0), (40, 60)),
                                 self.spritesheet.subsurface((120, 0), (40, 60)),
                                 self.spritesheet.subsurface((160, 0), (40, 60)),
                                 self.spritesheet.subsurface((200, 0), (40, 60)),]
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
                                 self.spritesheet.subsurface((200, 120), (40, 60)),]
        self.sprites_cima = [self.spritesheet.subsurface((0, 180), (40, 60)),
                                 self.spritesheet.subsurface((40, 180), (40, 60)),
                                 self.spritesheet.subsurface((80, 180), (40, 60)),
                                 self.spritesheet.subsurface((120, 180), (40, 60)),
                                 self.spritesheet.subsurface((160, 180), (40, 60)),
                                 self.spritesheet.subsurface((200, 180), (40, 60)),]
        self.image = self.sprites_direita[2]
        self.rect = self.image.get_rect(center=(w//2, h//2))

    # metodo de movimentacao da classe jogador
    def movimentacao(self, tecla):

        if tecla[pygame.K_UP] and self.rect.y > 0:
            self.parado = False
            self.direcao = 'cima'
            self.rect.y -= self.vel

        elif tecla[pygame.K_RIGHT] and self.rect.x < 750:
            self.parado = False
            self.direcao = 'direita'
            self.rect.x += self.vel

        elif tecla[pygame.K_DOWN] and self.rect.y < 400:
            self.parado = False
            self.direcao = 'baixo'
            self.rect.y += self.vel

        elif tecla[pygame.K_LEFT] and self.rect.x > 0:
            self.parado = False
            self.direcao = 'esquerda'
            self.rect.x -= self.vel

        else:
            self.parado = True

    # metodo de animacao
    def animacao(self):
        if self.parado:
            if self.direcao == 'direita':
                self.image = self.sprites_direita[2]
            elif self.direcao == 'esquerda':
                self.image = self.sprites_esquerda[0]
            elif self.direcao == 'cima':
                self.image = self.sprites_cima[0]
            elif self.direcao == 'baixo':
                self.image = self.sprites_baixo[0]
        else:
            self.contador += 0.5
            if self.contador == 6:
                self.contador = 0
            if self.direcao == 'direita':
                self.image = self.sprites_direita[int(self.contador)]
            elif self.direcao == 'esquerda':
                self.image = self.sprites_esquerda[int(self.contador)]
            elif self.direcao == 'cima':
                self.image = self.sprites_cima[int(self.contador)]
            elif self.direcao == 'baixo':
                self.image = self.sprites_baixo[int(self.contador)]

    def colisao_item_vel(self, item):
        if self.rect.colliderect(item):
            self.coleta_vel = True
        else:
            self.coleta_vel = False

    def colisao_item_vida(self, item):
        if self.rect.colliderect(item):
            if self.vida < 3:
                self.vida += 1
            self.coleta_vida = True
        else:
            self.coleta_vida = False

    def colisao_item_ponto(self, item):
        if self.rect.colliderect(item):
            self.ponto += 10
            self.coleta_ponto = True
        else:
            self.coleta_ponto = False

    def colisao_flor(self, flor):
        if self.rect.colliderect(flor):
            self.vida -= 1
            self.dano = True
        else:
            self.dano = False

    # metodo de atualizacao de estado de jogo
    def game_over(self):
        if self.vida <= 0:
            self.morto = True

    # metodo que invoca os outros metodos para atualizar o jogo
    def update_jogador(self, items_vel, items_vida, items_ponto, flor, tecla):
        self.colisao_item_vel(items_vel)
        self.colisao_item_vida(items_vida)
        self.colisao_item_ponto(items_ponto)
        self.colisao_flor(flor)
        self.game_over()
        self.movimentacao(tecla)
        self.animacao()
        self.colisao_item_vel(items_vel)
