import pygame, sys
from pygame.math import Vector2
from jogador import Jogador
from vida import Vida
from velocidade import Velocidade
import numpy as np


# Classe que ira conter todos os objetos
class Main:
    def __init__(self):
        self.tela = pygame.display.get_surface()
        self.jogador = Jogador()
        self.item_vida = Vida()
        self.item_vel = Velocidade()
        self.next_move = pygame.time.get_ticks() + 100
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel)

    def update(self, inimigos, items_vel, items_vida, items_ponto, tecla):
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 100
            self.jogador.update_jogador(inimigos, items_vel, items_vida, items_ponto, tecla)
        self.item_vida.spawn_vida(self.jogador.coleta_vida)
        self.item_vel.spawn_velocidade(self.jogador.coleta_vel)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador, self.item_vida, self.item_vel)

    def draw_elementos(self):
        self.sprites.draw(self.tela)


if __name__ == '__main__':
    unidade = 20
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 22.5

    clock = pygame.time.Clock()
    clock.tick(30)

    bg = pygame.image.load("sprites/background.png")
    bg = pygame.transform.scale(bg, (unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))

    inimigo_pos = Vector2(np.random.randint(0, (unidade * SCREEN_WIDTH) - 22), np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22))
    item_ponto_pos = Vector2(np.random.randint(0, (unidade * SCREEN_WIDTH) - 22), np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22))
    inimigo = pygame.Rect(inimigo_pos.x, inimigo_pos.y, 22, 22)
    item_ponto = pygame.Rect(item_ponto_pos.x, item_ponto_pos.y, 22, 22)

    screen = pygame.display.set_mode((unidade * SCREEN_WIDTH, unidade * SCREEN_HEIGHT))
    pygame.display.set_caption('playground')

    running = True

    pygame.init()

    jogo = Main()

    while running:
        antiga_pontuacao = jogo.jogador.ponto
        antiga_vida = jogo.jogador.vida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        print((jogo.item_vel.rect.x, jogo.item_vel.rect.y))

        if jogo.jogador.morto:
            running = False

        tecla = pygame.key.get_pressed()
        jogo.update([inimigo], jogo.item_vel.rect, jogo.item_vida.rect, [item_ponto], tecla)
        jogo.jogador.vel = jogo.item_vel.vel

        if jogo.jogador.ponto != antiga_pontuacao:
            item_ponto = pygame.Rect(np.random.randint(0, (unidade * SCREEN_WIDTH) - unidade),
                                     np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22), 22, 22)
        if jogo.jogador.vida < antiga_vida:
            inimigo = pygame.Rect(np.random.randint(0, (unidade * SCREEN_WIDTH) - unidade),
                                     np.random.randint(0, (unidade * SCREEN_HEIGHT) - 22), 22, 22)
        
        pygame.display.update()
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))
        jogo.draw_elementos()
        pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), inimigo)
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 255), item_ponto)
        pygame.display.flip()
        clock.tick(30)
