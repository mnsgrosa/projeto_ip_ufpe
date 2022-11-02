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
        self.pos = Vector2(w // 2, h // 2)
        self.vida = 3
        self.vel = w // 40
        self.ponto = 0
        self.morto = False
        self.coleta_vida = False
        self.coleta_vel = False
        self.coleta_ponto = False
        self.contador = -0.25
        self.parado = True
        self.direcao = 'direita'
        self.direita_spritesheet = pygame.image.load('sprites/soldado_direita_spritesheet.png')
        self.sprites_direita = [scale(self.direita_spritesheet.subsurface((0, 0), (50, 30)), (75, 45)),
                                scale(self.direita_spritesheet.subsurface((0, 30), (50, 30)), (75, 45)),
                                scale(self.direita_spritesheet.subsurface((0, 60), (50, 30)), (75, 45))]
        self.esquerda_spritesheet = pygame.image.load('sprites/soldado_esquerda_spritesheet.png')
        self.sprites_esquerda = [scale(self.esquerda_spritesheet.subsurface((0, 0), (50, 30)), (75, 45)),
                                scale(self.esquerda_spritesheet.subsurface((0, 30), (50, 30)), (75, 45)),
                                scale(self.esquerda_spritesheet.subsurface((0, 60), (50, 30)), (75, 45))]
        self.cima_spritesheet = pygame.image.load('sprites/soldado_cima_spritesheet.png')
        self.sprites_cima = [scale(self.cima_spritesheet.subsurface((0, 0), (30, 46)), (45, 69)),
                            scale(self.cima_spritesheet.subsurface((30, 0), (30, 46)), (45, 69)),
                            scale(self.cima_spritesheet.subsurface((60, 0), (30, 46)), (45, 69))]
        self.baixo_spritesheet = pygame.image.load('sprites/soldado_baixo_spritesheet.png')
        self.sprites_baixo = [scale(self.baixo_spritesheet.subsurface((0, 0), (30, 46)), (45, 69)),
                            scale(self.baixo_spritesheet.subsurface((30, 0), (30, 46)), (45, 69)),
                            scale(self.baixo_spritesheet.subsurface((60, 0), (30, 46)), (45, 69))]
        self.image = self.sprites_direita[2]
        self.rect = self.image.get_rect(center=(w//2, h//2))

    # metodo de movimentacao da classe jogador
    def movimentacao(self, tecla):
        if tecla[pygame.K_UP] and self.pos.y > 0:
            self.parado = False
            self.direcao = 'cima'
            self.rect.y -= self.vel

        elif tecla[pygame.K_RIGHT] and self.pos.x < 800:
            self.parado = False
            self.direcao = 'direita'
            self.rect.x += self.vel

        elif tecla[pygame.K_DOWN] and self.pos.y < 450:
            self.parado = False
            self.direcao = 'baixo'
            self.rect.y += self.vel

        elif tecla[pygame.K_LEFT] and self.pos.x > 0:
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
                self.image = self.sprites_esquerda[2]
            elif self.direcao == 'cima':
                self.image = self.sprites_cima[2]
            elif self.direcao == 'baixo':
                self.image = self.sprites_baixo[2]
        else:
            self.contador += 0.25
            if self.contador > 2:
                self.contador = 0
            if self.direcao == 'direita':
                self.image = self.sprites_direita[int(self.contador)]
            elif self.direcao == 'esquerda':
                self.image = self.sprites_esquerda[int(self.contador)]
            elif self.direcao == 'cima':
                self.image = self.sprites_cima[int(self.contador)]
            elif self.direcao == 'baixo':
                self.image = self.sprites_baixo[int(self.contador)]


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

    def colisao_item_ponto(self, item):
        if self.rect.colliderect(item):
            self.ponto += 10
            self.coleta_ponto = True
        else:
            self.coleta_ponto = False

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
