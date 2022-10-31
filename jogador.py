import pygame
import math
from bala import Bala
from pygame.math import Vector2


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
        self.image = pygame.image.load('sprites/zezinho_parado.png')
        self.rect = self.image.get_rect()
        self.rect.x = w // 2
        self.rect.y = h // 2

    # metodo de movimentacao da classe jogador
    def movimentacao(self, tecla):
        if tecla[pygame.K_UP] and self.pos.y > 0:
            self.rect.y -= self.vel

        if tecla[pygame.K_RIGHT] and self.pos.x < 800:
            self.rect.x += self.vel

        if tecla[pygame.K_DOWN] and self.pos.y < 450:
            self.rect.y += self.vel

        if tecla[pygame.K_LEFT] and self.pos.x > 0:
            self.rect.x -= self.vel

    # metodo de animacao
    def draw_jogador(self):
        x_pos = self.pos.x
        y_pos = self.pos.y

        self.rect = pygame.Rect(x_pos, y_pos, 20, 20)
        pygame.draw.rect(pygame.display.get_surface(), (183, 111, 122), self.rect)

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
        return self.colisao_item_vel(items_vel)
