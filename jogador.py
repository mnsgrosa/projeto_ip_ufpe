import pygame
from pygame.math import Vector2


class Jogador:
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self.pos = Vector2(w // 2, h // 2)
        self.vida = 10
        self.vel = 0.000000001
        self.ponto = 0
        self.block = pygame.Rect(self.pos.x, self.pos.y, 20, 20)
        self.morto = False

    def movimentacao(self, tecla):
        if tecla[pygame.K_UP] and self.pos.y > 0:
            self.pos.y -= self.vel

        if tecla[pygame.K_RIGHT] and self.pos.x < 800:
            self.pos.x += self.vel

        if tecla[pygame.K_DOWN] and self.pos.y < 450:
            self.pos.y += self.vel

        if tecla[pygame.K_LEFT] and self.pos.x > 0:
            self.pos.x -= self.vel

    def draw_jogador(self):
        x_pos = self.pos.x
        y_pos = self.pos.y

        self.block = pygame.Rect(x_pos, y_pos, 20, 20)
        pygame.draw.rect(pygame.display.get_surface(), (183, 111, 122), self.block)

    def colisao_inimigos(self, enemy):
        colisao = self.block.collidelist(enemy)
        if colisao != -1:
            vida -= 1

    def colisao_item_vel(self, item):
        colisao = self.block.collidelist(item)
        if colisao:
            self.vel += 10

    def colisao_item_vida(self, item):
        colisao = self.block.collidelist(item)
        if colisao and self.vida < 10:
            self.vida += 1

    def colisao_item_ponto(self, item):
        colisao = self.block.collidelist(item)
        if colisao:
            self.ponto += 10

    def game_over(self):
        if self.vida <= 0:
            self.morto = True

    def update_jogador(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        self.colisao_inimigos(inimigos)
        self.colisao_item_vel(items_vel)
        self.colisao_item_vida(items_vida)
        self.colisao_item_ponto(items_ponto)
        self.movimentacao(tecla)