import pygame
import math
from bala import Bala
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
        self.coleta_vida = False
        self.coleta_vel = False
        self.ponto_coletado = (1000, 1000)
        self.contador = -0.5
        self.parado = True
        self.direcao = 'direita'
        self.direita_spritesheet = scale(pygame.image.load('sprites/soldado_direita_spritesheet.png'), (75, 135))
        self.sprites_direita = [self.direita_spritesheet.subsurface((0, 0), (75, 45)),
                                self.direita_spritesheet.subsurface((0, 90), (75, 45)),
                                self.direita_spritesheet.subsurface((0, 45), (75, 45)),
                                self.direita_spritesheet.subsurface((0, 90), (75, 45))]
        self.esquerda_spritesheet = scale(pygame.image.load('sprites/soldado_esquerda_spritesheet.png'), (75, 135))
        self.sprites_esquerda = [self.esquerda_spritesheet.subsurface((0, 0), (75, 45)),
                                 self.esquerda_spritesheet.subsurface((0, 90), (75, 45)),
                                 self.esquerda_spritesheet.subsurface((0, 45), (75, 45)),
                                 self.esquerda_spritesheet.subsurface((0, 90), (75, 45))]
        self.cima_spritesheet = scale(pygame.image.load('sprites/soldado_cima_spritesheet.png'), (135, 75))
        self.sprites_cima = [self.cima_spritesheet.subsurface((0, 0), (45, 75)),
                             self.cima_spritesheet.subsurface((90, 0), (45, 75)),
                             self.cima_spritesheet.subsurface((45, 0), (45, 75)),
                             self.cima_spritesheet.subsurface((90, 0), (45, 75))]
        self.baixo_spritesheet = scale(pygame.image.load('sprites/soldado_baixo_spritesheet.png'), (135, 75))
        self.sprites_baixo = [self.baixo_spritesheet.subsurface((0, 0), (45, 75)),
                              self.baixo_spritesheet.subsurface((90, 0), (45, 75)),
                              self.baixo_spritesheet.subsurface((45, 0), (45, 75)),
                              self.baixo_spritesheet.subsurface((90, 0), (45, 75))]
        self.direita_cima_spritesheet = scale(pygame.image.load('sprites/soldado_direita_cima_spritesheet.png'), (90, 180))
        self.sprites_direita_cima = [self.direita_cima_spritesheet.subsurface((0, 0), (90, 60)),
                                     self.direita_cima_spritesheet.subsurface((0, 120), (90, 60)),
                                     self.direita_cima_spritesheet.subsurface((0, 60), (90, 60)),
                                     self.direita_cima_spritesheet.subsurface((0, 120), (90, 60))]
        self.esquerda_cima_spritesheet = scale(pygame.image.load('sprites/soldado_esquerda_cima_spritesheet.png'), (90, 180))
        self.sprites_esquerda_cima = [self.esquerda_cima_spritesheet.subsurface((0, 0), (90, 60)),
                                     self.esquerda_cima_spritesheet.subsurface((0, 120), (90, 60)),
                                     self.esquerda_cima_spritesheet.subsurface((0, 60), (90, 60)),
                                     self.esquerda_cima_spritesheet.subsurface((0, 120), (90, 60))]
        self.esquerda_baixo_spritesheet = scale(pygame.image.load('sprites/soldado_esquerda_baixo_spritesheet.png'), (90, 180))
        self.sprites_esquerda_baixo = [self.esquerda_baixo_spritesheet.subsurface((0, 0), (90, 60)),
                                      self.esquerda_baixo_spritesheet.subsurface((0, 120), (90, 60)),
                                      self.esquerda_baixo_spritesheet.subsurface((0, 60), (90, 60)),
                                      self.esquerda_baixo_spritesheet.subsurface((0, 120), (90, 60))]
        self.direita_baixo_spritesheet = scale(pygame.image.load('sprites/soldado_direita_baixo_spritesheet.png'), (90, 180))
        self.sprites_direita_baixo = [self.direita_baixo_spritesheet.subsurface((0, 0), (90, 60)),
                                     self.direita_baixo_spritesheet.subsurface((0, 120), (90, 60)),
                                     self.direita_baixo_spritesheet.subsurface((0, 60), (90, 60)),
                                     self.direita_baixo_spritesheet.subsurface((0, 120), (90, 60))]
        self.image = self.sprites_direita[1]
        self.rect = self.image.get_rect(center=(w//2, h//2))

    # metodo de movimentacao da classe jogador
    def movimentacao(self, tecla):
        if tecla[pygame.K_RIGHT] and tecla[pygame.K_UP] and self.rect.x < 710 and self.rect.y > 0:
            self.parado = False
            self.direcao = 'direita cima'
            self.rect.x += self.vel
            self.rect.y -= self.vel

        elif tecla[pygame.K_LEFT] and tecla[pygame.K_UP] and self.rect.x > 0 and self.rect.y > 0:
            self.parado = False
            self.direcao = 'esquerda cima'
            self.rect.x -= self.vel
            self.rect.y -= self.vel

        elif tecla[pygame.K_LEFT] and tecla[pygame.K_DOWN] and self.rect.x > 0 and self.rect.y < 390:
            self.parado = False
            self.direcao = 'esquerda baixo'
            self.rect.x -= self.vel
            self.rect.y += self.vel

        elif tecla[pygame.K_RIGHT] and tecla[pygame.K_DOWN] and self.rect.x < 710 and self.rect.y < 390:
            self.parado = False
            self.direcao = 'direita baixo'
            self.rect.x += self.vel
            self.rect.y += self.vel

        elif tecla[pygame.K_UP] and self.rect.y > 0:
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
                self.image = self.sprites_direita[1]
            elif self.direcao == 'esquerda':
                self.image = self.sprites_esquerda[1]
            elif self.direcao == 'cima':
                self.image = self.sprites_cima[1]
            elif self.direcao == 'baixo':
                self.image = self.sprites_baixo[1]
            elif self.direcao == 'direita cima':
                self.image = self.sprites_direita_cima[1]
            elif self.direcao == 'esquerda cima':
                self.image = self.sprites_esquerda_cima[1]
            elif self.direcao == 'esquerda baixo':
                self.image = self.sprites_esquerda_baixo[1]
            elif self.direcao == 'direita baixo':
                self.image = self.sprites_direita_baixo[1]
        else:
            self.contador += 0.5
            if self.contador == 4:
                self.contador = 0
            if self.direcao == 'direita':
                self.image = self.sprites_direita[int(self.contador)]
            elif self.direcao == 'esquerda':
                self.image = self.sprites_esquerda[int(self.contador)]
            elif self.direcao == 'cima':
                self.image = self.sprites_cima[int(self.contador)]
            elif self.direcao == 'baixo':
                self.image = self.sprites_baixo[int(self.contador)]
            elif self.direcao == 'direita cima':
                self.image = self.sprites_direita_cima[int(self.contador)]
            elif self.direcao == 'esquerda cima':
                self.image = self.sprites_esquerda_cima[int(self.contador)]
            elif self.direcao == 'esquerda baixo':
                self.image = self.sprites_esquerda_baixo[int(self.contador)]
            elif self.direcao == 'direita baixo':
                self.image = self.sprites_direita_baixo[int(self.contador)]


    # metodo de colisao dos outros items, o parametro recebe uma lista de items
    # e verifica se colidiu com os itens ou inimigos. prevejo que depois teirei de
    # saber com qual objeto detectou colisao
    def colisao_inimigos(self, enemy):
        lista_colisao = []
        for inimigo in enemy:
            if self.rect.colliderect(inimigo):
                lista_colisao.append(True)
            else:
                lista_colisao.append(False)
        if True in lista_colisao:
            self.vida -= 1

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

    def colisao_item_ponto(self, lista_ponto):
        for ponto in lista_ponto:
            ponto_rect = pygame.Rect(ponto[0], ponto[1], 35, 35)
            if self.rect.colliderect(ponto_rect):
                self.ponto += 10
                self.ponto_coletado = ponto

    # metodo de atualizacao de estado de jogo
    def game_over(self):
        if self.vida <= 0:
            self.morto = True

    def atira(self, lista_de_inimigos):
        min_dist = float('inf')
        for inimigo in lista_de_inimigos:
            temp = math.sqrt((self.rect.x - inimigo.x) ** 2 + (self.rect.y - inimigo.y) ** 2)
            if temp < min_dist:
                min_dist = temp
                alvo = inimigo
        return Bala(alvo, self.rect.x, self.rect.y)

    # metodo que invoca os outros metodos para atualizar o jogo
    def update_jogador(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        self.colisao_inimigos(inimigos)
        self.colisao_item_vel(items_vel)
        self.colisao_item_vida(items_vida)
        self.colisao_item_ponto(items_ponto)
        self.game_over()
        self.movimentacao(tecla)
        self.animacao()
        return self.colisao_item_vel(items_vel)
