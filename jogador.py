import pygame
from pygame.math import Vector2


class Jogador:
    # construtor da classe do jogador
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self.pos = Vector2(w // 2, h // 2)
        self.vida = 10
        self.vel = w//40
        self.ponto = 0
        self.block = pygame.Rect(self.pos.x, self.pos.y, 20, 20)
        self.morto = False
        self.coleta_vida = False
        self.coleta_vel = False
        self.coleta_ponto = False

    # metodo de movimentacao da classe jogador
    def movimentacao(self, tecla):
        if tecla[pygame.K_UP] and self.pos.y > 0:
            self.pos.y -= self.vel

        if tecla[pygame.K_RIGHT] and self.pos.x < 800:
            self.pos.x += self.vel

        if tecla[pygame.K_DOWN] and self.pos.y < 450:
            self.pos.y += self.vel

        if tecla[pygame.K_LEFT] and self.pos.x > 0:
            self.pos.x -= self.vel
    
    # metodo de animacao
    def draw_jogador(self):
        x_pos = self.pos.x
        y_pos = self.pos.y

        self.block = pygame.Rect(x_pos, y_pos, 20, 20)
        pygame.draw.rect(pygame.display.get_surface(), (183, 111, 122), self.block)

    # metodo de colisao dos outros items, o parametro recebe uma lista de items
    # e verifica se colidiu com os itens ou inimigos. prevejo que depois teirei de
    # saber com qual objeto detectou colisao
    def colisao_inimigos(self, enemy):
        lista_colisao = []
        for inimigo in enemy:
            if self.block.colliderect(inimigo):
                lista_colisao.append(True)
            else:
                lista_colisao.append(False)
        if True in lista_colisao:
            self.vida -= 1

    def colisao_item_vel(self, item):
        if self.block.colliderect(item):
            return True

    def colisao_item_vida(self, item):
        if self.block.colliderect(item):
            self.vida += 1
            self.coleta_vida = True
        

    def colisao_item_ponto(self, item):
        lista_colisao = []
        for ponto in item:
            if self.block.colliderect(ponto):
                lista_colisao.append(True)
            else:
                lista_colisao.append(False)
        if True in lista_colisao:
            self.ponto += 10
            return True

    # metodo de atualizacao de estado de jogo
    def game_over(self):
        if self.vida <= 0:
            self.morto = True

    # metodo que invoca os outros metodos para atualizar o jogo
    def update_jogador(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        self.colisao_inimigos(inimigos)
        self.colisao_item_vel(items_vel)
        self.colisao_item_vida(items_vida)
        self.colisao_item_ponto(items_ponto)
        self.game_over()
        self.movimentacao(tecla)
        return self.colisao_item_vel(items_vel)